# my comment => single line comments

"""
Multi-line comment: 
Comments add extra information to your system. 
KISS( Keep is Stupid Simple)
"""

# ==================================================================================

"""
Python language: Collection of code that allows one to be able to write python code exposed via an API.
- Key-words eg and, or, for, if, while, do .. 
- inbuilt methods

"""

# print("Hello World!", "Hello Dunia", "Habari Dunia", sep=" <==>" ) 
# print("Omni-World!", "Hello Dunia", "Habari Dunia", sep=" <==>") 

"""
# VARIABLES: 
 - containers that hold something
 - linked to the memory
 - type inference (automatically inferes the data type)
 - scope(Local or Global)

 ===== RULE =====
 - Name is it as per what is actually is eg firstName or lastName, accessToken
 - choose either camelCase(firstName or lastName) or snake_case(first_name or last_name)
 - do not use in-built keywords eg and, or if
 - do not start with a number or a special character
 KISS**

"""
# global variables
firstName = "John"
secondName = "Doe"

#  std.input 
# lastName = input("Enter Last Name: ")

# print statements are std.outputs
# print(firstName, end=" ")
# print(secondName)
# print(firstName, secondName, lastName)
# print(firstName + secondName)


"""
FUNCTIONS: 
 - does something
 - group related procedure into one "call"
 - parameterized functions
 - non-parameterized function 

==== RULE ====
- must have "def" keyword 
- must have a functionName ( comply to naming methods eg camelCase or snake case)
- must have a parenthesis () + colon: eg ():
- everything inside it must have an indentation of 4 spaces press tab to create the spaces
- MUST do one thing only #singlePurpose
"""

#  DEFINE-ing plain function 
def greetings():
    print("Hellow Human!")

# CALL-ing a function
greetings()

# parameterized function
def greetHuman(name):
    print("Hellow", name)
 
#  function with return statement ( returns a value from the function)
def fetchTiktokVideos():
    print("fetching videos")
    return {"author":"John Anime", "video":"anime.vid"}
 

"""
ROCK PAPER SCISSORS
user1 gets rock user2 gets paper => user2 wins
user1 gets paper user2 gets paper => its a tie
user1 gets paper user2 gets scissors => user 2 wins
  
"""

# adding an external tool => random
import random

#list
itemChoices = ["rock", "paper", "scissors"] 
  

def getChoices():
    playerChoice = input("Kindly pick a choice(rock, paper or scissors): ")
    computerChoice =  random.choice(itemChoices) 
    return playerChoice, computerChoice


#  get winner
def getWinner(playerChoice, computerChoice):
    print("You chose: ", playerChoice, "Computer chose: ",computerChoice)
    if playerChoice == computerChoice:
        print("It's a tie!")

    elif playerChoice =="rock":
        if computerChoice == "paper":
            print("Paper covers rock. You lose!")
        elif computerChoice == "scissors":
            print("Rock smashes scissor. You win!")

    elif playerChoice =="paper":
        if computerChoice == "rock":
            print("Paper covers rock. You win!")
        elif computerChoice == "scissors":
            print("Scissors cut paper. You lose!")

    elif playerChoice =="scissors":
        if computerChoice == "rock":
            print("ock smashes scissor. You lose!")
        elif computerChoice == "paper":
            print("Scissors cut paper. You win!")


player, computer = getChoices()
getWinner(player, computer)
 
