"""
Data-types (strings, numbers(int, float, complex), bool, list, tuple, dict, set)
Operations + Operands, ENUMS
DATA STRUCTURES

"""


"""
- DATA-types
- operators & operands # "computations" 
- Object Oriented programming
- Data Structure (fundamentals)


BUILD: Webserver

"""


"""
Operators & Operands: 

- Arithmetic operators: +,- ,/, //, %, *, **
- assignment operator: = 
- Comparison Operators(acts as a predicate): ==, !=, <, >,<=, >=  
- Boolean operators(Truth table): and, or, not 
- is: identity operator
- in: membership operator
- bitwise(binary data/ information): &,|, ^, ~, <<, >> **


NOTE: 
when reassiigning a value of a variable we call that process variable overriding
"""
 

# Arithmetic operators: +,- ,/, //, %, *, **
num1 = 10
num2 = 20
num1 = 2 # variable overriding
num2 = 9 # variable overriding
output = num2 + num1 # addition
output = num2 - num1 # sub-traction
output = num2 / num1 # division
output = num2 // num1 # floor division
output = num2 % num1 # modulus => returns the remainder
output = num2 * num1 # multiplication
output = num2 ** num1 # multiplication



# Comparison Operators(acts as a predicate): ==, !=, <, >,<=, >=  (the data types must match)
num1 = 100 
num2 = 200
num3 ="100"
firstName = "Eren"
secondName = "Johnes"
output = num1 == num2 # checks for equality
output = num1 != num2 # checks that num1 is not equal to num2
output = firstName == secondName # checks that firstName is not equal to secondName
output = num1 == num3 # checks for equality
output = num1 > num2 # greater than
output = num1 <  num2 # less than exclusive of num2
output = num1 >=  num2 # greater than or equal to : inclusive of num2
output = num1 <=  num2 # less than or equal to inclusive of  num2


# Boolean operators(Truth table): and, or, not ( we are guided by a truth table)

firstName = "John"
secondName = "Doe"
age = 18
yob = 2015

if firstName == "John" and age < 18:
    output = "Welcome John, you are under 18yrs old, you can play with the small swings!"
elif secondName =="Doe" and age >= 18:
    output = "Take care of the kids as they play."
else:
    output = "You are allowed to play with the adult swings!"
 

if firstName == "Johne" or age < 18:
    output = "Welcome John, you are under 18yrs old, you can play with the small swings!"
elif secondName =="Doe" or age >= 18:
    output = "Take care of the kids as they play."
else:
    output = "You are allowed to play with the adult swings!"

output = not firstName == "John"    


# is: identity operator and   in: membership operator
firstName = "Jane"
secondName = "Mary"
age = 45
fruits = ["apple", "mango", "banana","pear"]

output =  secondName is firstName # is acts as an idntity operator answers the quester "is it equal to"
output = 'n' in firstName # in is  membership operator answers the question "is it fonud in ..."
output = "mango" in fruits



# ENUM: put together the related constants. 
from enum import Enum

class LoginState(Enum):
    IN_ACTIVE = 0
    ACTIVE =1

output = LoginState.ACTIVE.value
output = LoginState.IN_ACTIVE.value

"""
DATA TYPES: 
- What entity do we place in a variable. 
- Boolean: True or False
- Numbers( int, float, complex)
- Strings
- Lists - []
- Tuples- ()
- Dictionary - {}
- Set- {}

from the above we create objects and each object has access ot dedicated methods
"""

# Boolean: True or False

isLoggedIn = True 
isProgressing = False

output = isLoggedIn
output = not isProgressing

# Numbers( int, float, complex)
#  int => -ve infinity to +ve infinity
num1 = 10 
num2 = -10
num =  int("100") # type cast => convert to integer
 
# float => 64Bbit, they decimal numbers   -ve infinity to +ve infinity
num3 = 0.3456
num4 = -1.34566

num =  float(num1) # convert to floating/ decimal
# complex  square root of 2 => complex number j
num5 = 2j
num =  complex(num1) # convert to complex number

output = num5
output = num


years = 100
output = f"HERO1: {firstName} || HERO2: {secondName} and they have been friends for {years}yrs"   

# Strings => collection of character but it is immutable
firstName = "Spiderman"
secondName = "Batman"
# string concatenation: +, comma, f-string
output = firstName + secondName # using +
output = firstName, secondName 
output = f"{firstName} {secondName}" #f-string

# String is a collection of characters => you can access each character using indexes
output = firstName[-1]

# slicing: select a portion of the actual string. nameOfString[start:end] end position = end - 1
output = firstName[0:6]
output = firstName[:-1]
output = firstName[-1:]
output = firstName[:]
output = firstName[2:]

# string methods
output = firstName.upper()
output = firstName.lower()
output = firstName.capitalize()
output = firstName.isalnum()


"""
List: 
- ordered
- a collection of items 
- it contain different data types of items
- accessed via indexes (makes it fast for accessing, deletion and updating values)** performance # O(1)
- insertion at specific points (takes up some significant compute)** performance O(n)
- represented using []
- mutable(change or update the elements) in nature 

 ===== RULE =====
 - Name is it as per what is actually is eg firstName or lastName, accessToken
 - choose either camelCase(firstName or lastName) or snake_case(first_name or last_name)
 - do not use in-built keywords eg and, or if
 - do not start with a number or a special character

"""
# list
fruits = ["apples", "mangoes", "banana", "pear", "pineapples"] 

output = fruits[2]# indexes
output = fruits[2:] #sclicing
output = fruits[2:4] #slicing

# fruits.pop() # removes and updates last element

output = len(fruits) # checks size of list
fruits.append("oranges")
fruits.insert(2,"watermelon") # computattionally expensive => 

output = "avocado" in fruits # membership
output = fruits




print("==================================================")
print(output)
print("==================================================")





















