"""
# 🎮 Tic Tac Toe Game (Python Console)

Welcome to a simple **Tic Tac Toe** game built using pure Python!  
This game supports 2-player mode in the terminal with the following features:

## ✅ Features:
- Interactive player input
- Dynamic board display
- Win condition checks for all directions
- Input validation and error prompts
- Option to replay the game

## 🎯 How to Play:
1. Each player selects either 'X' or 'O'.
2. Players take turns picking a position from 1 to 9.
3. The first player to align 3 marks (row/column/diagonal) wins.
4. If all cells are filled and there's no winner, it's a tie.

## 📌 Position Reference:
Here's the board layout with positions:

 7 | 8 | 9  
-----------
 4 | 5 | 6  
-----------
 1 | 2 | 3  

## 👨‍💻 Author
Made with ❤️ using basic Python concepts.

Enjoy playing!
"""

# We need to print a board.
def display_board(board):
    print(chr(27) + "[2J")
    print(f'{board[6]}' + ' | ' + f'{board[7]}' + ' | ' + f'{board[8]}')
    print('-----------')
    print(f'{board[3]}' + ' | ' + f'{board[4]}' + ' | ' + f'{board[5]}')
    print('-----------')
    print(f'{board[0]}' + ' | ' + f'{board[1]}' + ' | ' + f'{board[2]}')

# Take in player input.
def player_input():
    choice = 'WRONG'

    while choice not in ['X','O']:
        choice = input('Pick a choice for Player- 1 (X or O): ')
        if choice not in ['X','O']:
          print('Sorry, I dont understand, Please choose X or O')
    if choice == 'X':
        return ['X','O']
    else:
        return ['O','X']
        
def place_marker(board,marking,position):
    board[position] = marking
    return board

def marker_input(playerId,choices_availaible):
  choice = 'WRONG'
  while choice not in [str(i) for i in choices_availaible]:
      choice = input(f'Pick a choice for Player- {playerId} ({choices_availaible}): ')
      if choice not in [str(i) for i in choices_availaible]:
        print(f'Sorry, I dont understand, Please choose between ({choices_availaible})')
  return int(choice) - 1

def win_check(board, mark):
    if(board[0] == board[1] == board[2] == mark):
      return True
    if(board[3] == board[4] == board[5] == mark):
      return True
    if(board[6] == board[7] == board[8] == mark):
      return True
    if(board[0] == board[3] == board[6] == mark):
      return True
    if(board[1] == board[4] == board[7] == mark):
      return True
    if(board[2] == board[5] == board[8] == mark):
      return True
    if(board[0] == board[4] == board[8] == mark):
      return True
    if(board[2] == board[4] == board[6] == mark):
      return True
    return False
# Place their input on the board.
  # display_board() after input
# Check if the game is won,tied, lost, or ongoing.
def check_score():
    print("check_score")
# Repeat c and d until the game has been won or tied.
#   player_input(), check_score()  
# Ask if players want to play again.
def game_on():
    choice = 'WRONG'
    while choice not in ['Y','N']:
        choice = input('Keep Playing? (Y or N): ')
        if choice not in ['Y','N']:
            print('Sorry, I dont understand, Please choose Y or N')
        else:
            break
    if choice == 'Y':
      return True
    return False

print('Welcome to Tic Tac Toe!')
game_on = True
while game_on:
  play_game = input('Are you ready to play? Enter Yes or No.')
  if play_game.lower()[0] == 'y':
    game_on = True
  else:
    game_on = False
  board =  [' '] * 10 
  choices_availaible = [1,2,3,4,5,6,7,8,9]
  player1Input = None
  player2Input = None
  [player1Input,player2Input] = player_input()

  is_win = False
  while is_win == False and len(choices_availaible) > 0:
    position_input = marker_input(1,choices_availaible)
    choices_availaible = [x for x in choices_availaible if x != (position_input + 1)]
    board = place_marker(board, player1Input, position_input)
    display_board(board)
  
    is_win = win_check(board,player1Input)
    if is_win == True:
      print('Player 1 Wins !!!')
      break
    position_input = marker_input(2,choices_availaible)
    choices_availaible = [x for x in choices_availaible if x != (position_input + 1)]
    board = place_marker(board, player2Input, position_input)
    display_board(board)
    is_win = win_check(board,player2Input)
    if is_win == True:
      print('Player 2 Wins !!!')
      break

print('Game Finished !!!!')

        