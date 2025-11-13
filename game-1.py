# RECIPE

"""
GAME: ROCK PAPER SCISSORS:

======= VARIABLES =======

Players(2):
    - playerOne
    - Computer

gameChoices(3):
    - "rock"
    - "paper"
    - "scissors"

choiceSelection:
    - playerOne selects option (enable the player to input their choice)
    - computer selects option (randomize it)


======= STEPS TO SOLVE  =======
- get playerOne and Computers selections and print them
- decide who wins (function):
    - EQUALity of selection == "it's a TIE!"
    - if playerOne= "rock":
        computer = "paper":
            - since paper covers rock: COMPUTER WINS!
        computer = "scissors":
            - since rock crashes scissors: {playerOneName} WIN!
    - if playerOne= "paper":
        computer = "rock":
            - since paper covers rock: {playerOneName} WIN!
        computer = "scissors":
            - since scissors cut paper: COMPUTER WINS!
    - if playerOne= "scissors":
        computer = "rock":
            - since rock crashes scissors: COMPUTER WINS!
        computer = "paper":
            - since scissors cut paper: {playerOneName} WIN!
"""
 

import random

gameChoices = ["rock", "paper", "scissors"]
output =""
 
# choice selection
def playerChoice():
    playerOneName = input("Enter your cool game_NAME! eg Hero X: ") 
    playerOneChoice = input("Pick your poison (rock, paper, scissors): ") 
    computerChoice = random.choice(gameChoices) # randomly select a game choice
    output = f"{playerOneName}: {playerOneChoice} || COMPUTER: {computerChoice}"
    print("\n\n********************** PLAYER MOVES ****************************")
    print(output)
    print("********************** PLAYER MOVES ****************************")
    return playerOneName, playerOneChoice, computerChoice

def decidePlayerWinner(playerOneName, playerOneChoice, computerChoice):
    if playerOneChoice == computerChoice:
        return "It's a TIE"

    elif playerOneChoice == "rock":
        if computerChoice == "paper":
            return  "since paper covers rock: COMPUTER WINS!"
        elif computerChoice == "scissors":
            return  f"since rock smashes scissors: {playerOneName} WINS!"

    elif playerOneChoice == "paper":
        if computerChoice == "rock":
            return  f"since paper covers rock: {playerOneName} WINS!"
        elif computerChoice == "scissors":
            return  "since scissors cut paper: COMPUTER WINS!"

    elif playerOneChoice == "scissors":
        if computerChoice == "rock":
            return  "since rock smashes scissors: COMPUTER WINS!"
        elif computerChoice == "paper":
            return  f"since scissors cut paper: {playerOneName} WINS!"

playerOneName, playerOneChoice, computerChoice = playerChoice()
output = decidePlayerWinner(playerOneName, playerOneChoice, computerChoice)

print("\n\n====================== RESULTS ============================")
print(output)
print("====================== RESULTS ============================")