from art import logo, vs
import random
from game_data import data
import os

# Format account data into printable format.
def format_account_data(account):
  name = account['name']
  description = account['description']
  country = account['country']
  return f'{name}, a {description}, from {country}'

## If Statement
def check_answer(guess, follower_a, follower_b):
  if follower_a > follower_b:
    return guess == 'a'
  else:
    return guess == 'b'

# Clear screen between rounds.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def game():
  print(logo)
  score = 0
  # Make game repeatable.
  account_b = random.choice(data)
  while True:
    # Generate a random account from the game data.
    # Make B become the next A.
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
      account_b = random.choice(data)
    
    print(f"Compare A: {format_account_data(account_a)}")
    print(vs)
    print(f"Against B: {format_account_data(account_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count.
    follower_a = account_a['follower_count']
    follower_b = account_b['follower_count']
    is_correct = check_answer(guess, follower_a, follower_b)

    cls()
    # Add art.
    print(logo)
    # Feedback.
    if is_correct:
      # Score Keeping.
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      break
game()
