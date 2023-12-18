# Solution by Angela
# note: write down the step and need first.
#       find what kind of function do you need


from art import logo
from random import randint

# make function to set difficulty
def set_difficulty(level):
  if level == 'easy':
    print('You have 10 attempts remaining to guess the number.')
    return 10
  elif level == 'hard':
    print('You have 5 attempts remaining to guess the number.')
    return 5

def game():
  print(logo)
  print('Welcome to the Number Guessing Game!')
  print('I\'m thinking of a number between 1 and 100.')
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  # choosing a random number between 1 and 100
  answer = randint(1, 100)
  turns = set_difficulty(level)

  # let the user guess a number
  guess = int(input('Make a guess: '))

  # repeat the guessing functionality if they get it wrong
  # check the guess against answer
  while guess != answer:
    turns -= 1
    if guess > answer:
      print('Too high.')
    elif guess < answer:
      print('Too low.')
    if turns == 0:
      print('You\'ve run out of guesses, you lose.')
      break
    print('Guess again.')
    print(f'You have {turns} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))

  if guess == answer:
    print(f'You got it! The answer was {answer}.')

game()