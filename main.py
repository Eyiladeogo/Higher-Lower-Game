from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print(logo)

game_over = False


def generate_celeb():
    """Generates a random celeb from the list"""
    random_celeb = data[random.randint(0, len(data) - 1)]
    return random_celeb


user_score = 0
celeb_1 = generate_celeb()
celeb_2 = generate_celeb()

while game_over != True:
  higher_celeb = max(celeb_1['follower_count'], celeb_2['follower_count'])
  user_input = (input(
      f"Compare A: {celeb_1['name']}, a {celeb_1['description']}, from {celeb_1['country']} \n\n {vs} \n\n Against B: {celeb_2['name']}, a {celeb_2['description']}, from {celeb_2['country']}\n Who has more followers? Type 'A' or 'B' ")).upper()
  # user_input = "A"
  clear()

  if user_input == "A" and celeb_1['follower_count'] == higher_celeb:
      user_score += 1
      print(f"You're right! Current Score: {user_score}")
      celeb_1 = celeb_1
      celeb_2 = generate_celeb()
  elif user_input == "A" and celeb_1['follower_count'] != higher_celeb:
      print(f"Sorry, that's wrong. Final Score: {user_score}")
      game_over = True
  elif user_input == "B" and celeb_1['follower_count'] == higher_celeb:
      print(f"Sorry, that's wrong. Final Score: {user_score}")
      game_over = True
  elif user_input == "B" and celeb_1['follower_count'] != higher_celeb:
      user_score += 1
      print(f"You're right! Current Score: {user_score}")
      celeb_1 = celeb_2
      celeb_2 = generate_celeb()
  
