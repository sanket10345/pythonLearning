import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
c1 = Card('Hearts','Two')


class Deck:
    def __init__(self):
      # Note this only happens once upon creation of a new Deck
      self.all_cards = [] 
      for suit in suits:
          for rank in ranks:
              # This assumes the Card class has already been defined!
              self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

myDeck = Deck()
myDeck.shuffle()

player_one = Player('one')
player_two = Player('two')


totalCards = len(myDeck.all_cards)
for i in range(totalCards // 2):
    player_one.add_cards(myDeck.deal_one())
    player_two.add_cards(myDeck.deal_one())

# print(player_one)
# print(player_two)

game_on = True
round_counter = 0

while game_on:
  round_counter+= 1
  print(f'Round - {round_counter}')

  if len(player_one.all_cards) == 0:
      print("Player One out of cards! Game Over")
      print("Player Two Wins!")
      game_on = False
      break
  if len(player_two.all_cards) == 0:
      print("Player Two out of cards! Game Over")
      print("Player One Wins!")
      game_on = False
      break
  
  player_one_cards = []
  player_two_cards = []
  player_one_cards.append(player_one.remove_one())
  player_two_cards.append(player_two.remove_one())
  
  at_war = True
  while at_war:
      if(player_one_cards[-1].value > player_two_cards[-1].value):
          player_one.add_cards(player_two_cards)
          player_one.add_cards(player_one_cards)
          at_war = False
      
      elif(player_one_cards[-1].value < player_two_cards[-1].value):
          player_two.add_cards(player_one_cards)
          player_two.add_cards(player_two_cards)
          at_war = False
      else:
          print('WAR!')
          if len(player_one.all_cards) < 5:
            print("Player One unable to play war! Game Over at War")
            print("Player Two Wins! Player One Loses!")
            game_on = False
            break

          elif len(player_two.all_cards) < 5:
            print("Player Two unable to play war! Game Over at War")
            print("Player One Wins! Player One Loses!")
            game_on = False
            break
            # Otherwise, we're still at war, so we'll add the next cards
          else:
            for num in range(5):
              player_one_cards.append(player_one.remove_one())
              player_two_cards.append(player_two.remove_one())

