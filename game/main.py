import random


def choose_options():
  options = ('rock', 'beats', 'scissors')
  user_option = input('rock, beats or scissors => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('invalid option!')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('user option =>', user_option)
  print('computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('draw!')
  elif user_option == 'rock':
    if computer_option == 'scissors':
      print('rock wins to scissors')
      print('user won!')
      user_wins += 1
    else:
      print('beats wins to rock')
      print('computer won!')
      computer_wins += 1
  elif user_option == 'beats':
    if computer_option == 'rock':
      print('beats wins to rock')
      print('user won')
      user_wins += 1
    else:
      print('scissors wins to beats')
      print('computer won!')
      computer_wins += 1
  elif user_option == 'scissors':
    if computer_option == 'beats':
      print('scissors wins to beats')
      print('user won!')
      user_wins += 1
    else:
      print('rock wins to scissors')
      print('computer won!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('the winner is the computer')
      break

    if user_wins == 2:
      print('the winner is the user')
      break

run_game()