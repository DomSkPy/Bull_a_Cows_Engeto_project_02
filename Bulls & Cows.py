"""
second_project.py: druhy projekt do Engeto Online Python Akademie
autor: Domnik Skrenek
email: skrenekD@gmail.com
discord: DomSk
"""
import random
line = 40 * "="
#Wellcome player
print("Hi!")
wellcome_user = input("What's your name?")
print(f"{line}",
      f"Welcome to the Bulls and Cows game, {wellcome_user}!",
      f"{line}",
      f"I've generated a random 4 digit number for you.",
      f"let's play a Bulls and Cows game.",
      f"{line}",
      sep="\n")

#Generate numbers
def generate_num():
    import random
    num_r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rand_num_cel = []

