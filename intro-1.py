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
print("==================================================")
print(output)
print("==================================================")





















