"""
ATM Facade Module

This module implements the Facade design pattern for an ATM system.
It provides a simplified interface (ATMFacade) to interact with complex subsystems:
  - CardReader: Card insertion and ejection
  - PINValidator: Secure PIN validation with lockout handling
  - AccountDatabase: Account balance management and transaction logging
  - CashDispenser: Cash inventory management and dispensing logic

Key Features:
  * Insertion/ejection of cards
  * PIN validation with maximum attempt enforcement and account locking
  * Atomic debit/credit operations, overdraft prevention, and transaction history
  * Cash dispensing algorithm with inventory checks and refill support

Typical Usage:
    atm = ATMFacade()
    atm.insert_card({"card_id": "card123"})
    try:
        atm.enter_pin("1234")
        dispensed = atm.withdraw(180)
        print("Dispensed:", dispensed)
    except Exception as e:
        print("Error:", e)
"""

import hmac
import hashlib
from typing import Dict, List, Tuple

# Exceptions
class InvalidPINException(Exception):
    pass

class CardLockedException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class InsufficientCashException(Exception):
    pass

class AccountNotFoundException(Exception):
    pass


class CardReader:
    def __init__(self):
        self.current_card_id = None

    def read_card(self, card_info: Dict) -> str:
        # Example: parse card_id
        self.current_card_id = card_info.get("card_id")
        return self.current_card_id

    def eject(self):
        self.current_card_id = None


class AccountDatabase:
    def __init__(self):
        # card_id -> account data
        self._accounts: Dict[str, Dict] = {}
        # transaction logs: list of tuples
        self._logs: List[Tuple[str, str, float, float]] = []

    @classmethod
    def load_from_source(cls):
        # For demo, we set up a sample account
        db = cls()
        # PIN '1234'
        pin_hash = hashlib.sha256(b'1234').hexdigest()
        db._accounts['card123'] = {
            'balance': 1000.0,
            'pin_hash': pin_hash,
            'overdraft_limit': 0.0,
            'locked': False
        }
        return db

    def get_pin_hash(self, card_id: str) -> str:
        acct = self._get_account(card_id)
        return acct['pin_hash']

    def get_balance(self, card_id: str) -> float:
        acct = self._get_account(card_id)
        if acct['locked']:
            raise CardLockedException("Account is locked")
        return acct['balance']

    def debit(self, card_id: str, amount: float):
        acct = self._get_account(card_id)
        if acct['locked']:
            raise CardLockedException("Account is locked")
        if acct['balance'] - amount < -acct['overdraft_limit']:
            raise InsufficientFundsException("Insufficient funds")
        acct['balance'] -= amount
        self._logs.append((card_id, 'debit', amount, acct['balance']))

    def credit(self, card_id: str, amount: float):
        acct = self._get_account(card_id)
        acct['balance'] += amount
        self._logs.append((card_id, 'credit', amount, acct['balance']))

    def get_transaction_history(self, card_id: str, limit: int = 10):
        return [log for log in self._logs if log[0] == card_id][-limit:]

    def lock_account(self, card_id: str):
        acct = self._get_account(card_id)
        acct['locked'] = True

    def unlock_account(self, card_id: str):
        acct = self._get_account(card_id)
        acct['locked'] = False

    def _get_account(self, card_id: str) -> Dict:
        if card_id not in self._accounts:
            raise AccountNotFoundException(f"No account for card ID {card_id}")
        return self._accounts[card_id]


class PINValidator:
    MAX_ATTEMPTS = 3

    def __init__(self, account_db: AccountDatabase):
        self._failed_attempts: Dict[str, int] = {}
        self._locked_cards: set = set()
        self._db = account_db

    def validate(self, card_id: str, entered_pin: str) -> bool:
        if card_id in self._locked_cards or self._db._accounts[card_id]['locked']:
            raise CardLockedException("Card is locked")

        stored_hash = self._db.get_pin_hash(card_id)
        entered_hash = hashlib.sha256(entered_pin.encode()).hexdigest()

        if not hmac.compare_digest(entered_hash, stored_hash):
            count = self._failed_attempts.get(card_id, 0) + 1
            self._failed_attempts[card_id] = count
            if count >= self.MAX_ATTEMPTS:
                self._locked_cards.add(card_id)
                self._db.lock_account(card_id)
                raise CardLockedException("Card locked due to too many invalid PINs")
            raise InvalidPINException("Invalid PIN")

        # success
        self._failed_attempts[card_id] = 0
        return True

    def reset(self, card_id: str):
        self._failed_attempts.pop(card_id, None)
        self._locked_cards.discard(card_id)
        self._db.unlock_account(card_id)


class CashDispenser:
    def __init__(self, initial_inventory: Dict[int, int] = None):
        self.inventory = initial_inventory or {}

    def check_availability(self, amount: int) -> bool:
        remaining = amount
        for denom in sorted(self.inventory.keys(), reverse=True):
            use = min(remaining // denom, self.inventory[denom])
            remaining -= use * denom
        return remaining == 0

    def dispense(self, amount: int) -> Dict[int, int]:
        if not self.check_availability(amount):
            raise InsufficientCashException("Cannot dispense requested amount")
        to_dispense: Dict[int, int] = {}
        for denom in sorted(self.inventory.keys(), reverse=True):
            count = min(amount // denom, self.inventory[denom])
            if count:
                to_dispense[denom] = count
                self.inventory[denom] -= count
                amount -= denom * count
        return to_dispense

    def refill(self, denomination: int, count: int):
        self.inventory[denomination] = self.inventory.get(denomination, 0) + count

    def get_inventory(self) -> Dict[int, int]:
        return dict(self.inventory)

    def total_cash_available(self) -> int:
        return sum(denom * cnt for denom, cnt in self.inventory.items())


class ATMFacade:
    def __init__(self):
        self.card_reader = CardReader()
        self.account_db = AccountDatabase.load_from_source()
        self.pin_validator = PINValidator(self.account_db)
        self.cash_dispenser = CashDispenser({100: 10, 50: 20, 20: 30, 10: 50})
        self.current_card_id: str = None

    def insert_card(self, card_info: Dict) -> None:
        self.current_card_id = self.card_reader.read_card(card_info)

    def enter_pin(self, pin_code: str) -> bool:
        return self.pin_validator.validate(self.current_card_id, pin_code)

    def withdraw(self, amount: int) -> Dict[int, int]:
        # Check balance
        balance = self.account_db.get_balance(self.current_card_id)
        if balance < amount:
            raise InsufficientFundsException("Insufficient funds")
        # Debit account
        self.account_db.debit(self.current_card_id, amount)
        # Dispense cash
        dispensed = self.cash_dispenser.dispense(amount)
        # Eject card
        self.eject_card()
        return dispensed

    def eject_card(self) -> None:
        self.card_reader.eject()
        self.current_card_id = None


# Example usage:
if __name__ == "__main__":
    atm = ATMFacade()
    card = {"card_id": "card123"}
    atm.insert_card(card)
    try:
        atm.enter_pin("1234")
        dispensed = atm.withdraw(180)
        print("Dispensed:", dispensed)
    except Exception as e:
        print("Error:", e)
