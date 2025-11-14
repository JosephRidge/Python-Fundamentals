"""
Data-types (strings, numbers(int, float, complex), bool, list, tuple, dict, set)
Operations + Operands, ENUMS
DATA STRUCTURES

control flows eg ternary operators

"""

output ="" # global variabel dedicated for print outs
# Strings => lists of characters. They are placed in between,either '' or "". String is immutable

# defining strings ie objects
petName = "Simba%&875"
fishName = 'Neemo'
owenership = 'This is Simba\'s Toy!'
owenership = "This is Simba's Toy!"

# string concatenation 
output = petName + fishName # combines strings but does not add a space in between 
output = petName, fishName
output = f"Dog: {petName} || Fish: {fishName}" # f-string=> combine variablesa with strings: interporlation

# access parts of a string using indexes and slicing
output = petName[0]#accessing via indexes
output = petName[1] #accessing via indexes 
output = len(petName)
output = petName[1:5] #slicing
output = owenership[2:4]#slicing ===>  [start: stop-1]

# methods
petName = "orlando"
output = petName.lower()
petName.upper()

name = petName+ " bloom"
output = name.title()

# type casting:
num=1
output = type(num)
num = str(num)
output = type(num)

# Boolean: True or False, is{CurrentState}
isLightOn = False
isWaterRunning = True
bool()# casting can be done using bool() constructor

# numbers( int, float, copmlex)
# integers -ve infinity to +ve infinity 
num1 = 10
num2 = -100
int("100") # used to convert it integer
output = type(int("100"))

# floating: decimal numbers -ve infinity to +ve infinity  (64bit)
lat = 0.34
lng = 36.43
num3 = 0.23456
num4 = -0.1234
float(10) # used to convert it integer
# output = float(23)

# complex* root 2 
num5 = 2j
complex(23) # used to convert it integer
# output = complex(23)

# constants: 
YEAR_OF_BIRTH = 10

#Enum 
from enum import Enum

class Color(Enum):
    PRIMARY = "blue"
    SECONDARY = "light-blue"

output = Color.PRIMARY.value

"""
 LISTS: 
    - Collections of items(can be of varying data types)
    - mutable
    - accesed via indexes
    - wrapped inside: []    
    - ordered 

"""


fruits  = ["apples", "mango", "pears", "bananas", "bananas", 1,2,3] # defined a list
output = fruits[1] # retreiving items using indexes
output  = fruits[0:3:2] # slicing

# size of lists
output = len(fruits)
output = "apples " in fruits
fruits  = ["apples", "mango", "pears", "bananas", "avocadoes", "tomatoes" ]
# manipulate it: Methods

fruits.append("pineapples") #add at the end
fruits.pop() #delete
fruits.remove("mango")# removes target element - computationally expensive
fruits.sort()

output = fruits

"""
TUPLES: 
    - defined using ()
    - immutable 
    - faster than list
    - collection of items
"""

planets = ("Earth", "Earth","Mars", "Uranus", "Jupiter", "Saturn")
output = planets.index("Jupiter") # get the index of a particular element


"""
Dictionary (dict, also called a hashmap):
    - representeed via {}
    - mutable 
    - key:value pair
     - retreiving elements is very fast

"""

student = {
    "name":"John Doe",
    "age":12,
    "year":2,
    "hasGraduated":False, 
    "course": "Mathematics"
}
# accesing elements
output = student["name"]
output = student["age"]

# methods
student.pop("name")
# student.clear()
student["family"] = "Superheros" # adding data
student.popitem()

output = student

"""
SET: 
    - unique items alone
    - wrapped inside: {}
    - set theory
"""
colors = {"blue", "green", "red", "red"}

fruits  = [ "mango", "pears", "mango", "pears", "pears", "mango", "pears", "bananas", "avocadoes", "tomatoes" ]

output = set(fruits)

colors.add("red")
colors.add("purple")
output = colors
 

print("===================================================") 
print(output)
print("===================================================")

