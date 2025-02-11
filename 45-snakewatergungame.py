#This is a game

import random

print("Welcome to Snake-Water-Gun game")

while True:
    player=input("Choose 'snake' or 'water' or 'gun' or 'exit'-If you want to exit the game\n")
    print("Player choice is:",player)
    
    if player == 'exit':
        print("Thanks you ! You are exited from game.")
        break
    if player not in ["snake","water","gun"]:
        print("Give your valid choice !")
        continue
    computer = random.choice(["snake","water","gun"])
    print("Computer choice is:",computer)
    if player == computer:
        print("Same choice,So its a tie!")
    elif(player == "snake" and computer == "water") or \
    (player == "water" and computer == "gun") or \
    (player == "gun" and computer == "snake"):
        print("You are the winner !")
    else:
        print("Computer is the winner!")
    print("-"*30)
