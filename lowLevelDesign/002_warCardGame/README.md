# War Card Game - Low-Level Design (LLD) Overview

## **1. Introduction**
This document provides a Low-Level Design (LLD) breakdown of the **War Card Game** implemented in Python. The game is a two-player card game where each player draws a card, and the player with the higher-ranked card wins the round. If both players draw a card of the same rank, a "War" occurs, requiring more cards to determine the winner.

## **2. Class Design (LLD)**

### **2.1 Card Class**
#### **Responsibilities:**
- Represents a single playing card with a **suit**, **rank**, and **value**.

#### **Attributes:**
- `suit (str)`: The suit of the card (e.g., Hearts, Diamonds, etc.).
- `rank (str)`: The rank of the card (e.g., Two, Three, Ace, etc.).
- `value (int)`: The numerical value of the card used for comparisons.

#### **Methods:**
- `__init__(suit, rank)`: Initializes a card with its suit, rank, and value.
- `__str__()`: Returns a string representation of the card.

### **2.2 Deck Class**
#### **Responsibilities:**
- Represents a full deck of **52 cards** and manages deck operations.

#### **Attributes:**
- `all_cards (list)`: A list containing all `Card` objects.

#### **Methods:**
- `__init__()`: Initializes a deck with 52 unique cards.
- `shuffle()`: Shuffles the deck randomly.
- `deal_one()`: Removes and returns a single card from the deck.

### **2.3 Player Class**
#### **Responsibilities:**
- Represents a player in the game and manages their hand of cards.

#### **Attributes:**
- `name (str)`: Name of the player.
- `all_cards (list)`: A list storing the player’s current cards.

#### **Methods:**
- `__init__(name)`: Initializes a player with a name and an empty hand.
- `remove_one()`: Removes and returns one card from the player's hand.
- `add_cards(new_cards)`: Adds one or multiple cards to the player's hand.
- `__str__()`: Returns a string representation of the player's current card count.

## **3. Game Flow**

### **3.1 Game Initialization**
1. A `Deck` object is created and shuffled.
2. Two `Player` objects (`player_one`, `player_two`) are created.
3. The deck is divided equally between the two players.

### **3.2 Round Execution**
1. Each player plays one card (removed from their hand).
2. The cards are compared based on their `value`.
   - The player with the **higher value** wins the round and takes both cards.
   - If values are **equal**, a "War" is declared.

### **3.3 Handling a "War"**
1. If a "War" occurs (same card value), each player places **five additional cards**.
2. The last card of the five is compared.
3. If a player does not have enough cards to continue the war, they **lose the game**.

### **3.4 Game Termination**
- The game continues **until one player has all the cards**.
- If a player runs out of cards, the opponent is declared the **winner**.

## **4. Code Structure**
```
/warCardGame/
│── warCardGame.py  # Main script containing all classes and game logic
│── README.md       # Game documentation (this file)
```

## **5. Design Decisions & Justifications**
- **Encapsulation**: Each entity (Card, Deck, Player) has clearly defined responsibilities.
- **Modularity**: The game logic is separate from the class definitions.
- **Scalability**: The current design allows easy modifications (e.g., different deck sizes or rules).
- **Randomness**: Uses Python's `random.shuffle()` for shuffling the deck.

## **6. Future Enhancements**
- Implement a graphical user interface (GUI).
- Add more configurable rules.
- Implement multiplayer online functionality.

---
This README provides a structured **LLD breakdown** of the **War Card Game**, ensuring clarity in class design and game logic.

