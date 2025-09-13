# File: homework1. py

# --- Variables and Data Types ---

variables = [10, 1.5, 3j, "hello", [1, 2, 3], {"name": "Ellen", "favorite fruit": "strawberry"}, (1,2), ["apple", "banana", "strawberry"], True, None, [True, "blue", 12], str(14), 1e4]
for variable in variables:
    print(variable)
    print(type(variable)) 

a = 10 #a is an integer, a whole number with no decimals
b = 1.5 #b is an integer, a whole number with no decimals
c = 3j #c is a complex number on the imaginary plane
d = "hello" #d is a string, a collection of characters treated as a single unit of text
e = [1, 2, 3] #e is a list used to store an ordered, changeable collection of items
f = {"name": "Ellen", "favorite fruit": "strawberry"} #f is a dictionary that stores data in key-value pairs, so each key maps to a specific value
g = (1,2) #g is a tuple, which stores an ordered and immutable collection of items in a single variable
h = ["apple", "banana", "strawberry"] #h is a list used to store an ordered, changeable collection of items
i = True #i is a Boolean that represents one of 2 truth values, True or False. It helps make decisions in code.
j = None #None represents the absence of a value, meaning a variable or object currently holds no value
k = [True, "blue", 12] #k is a list used to store an ordered, changeable collection of items
l = str(14) #l is a string. the str() function converts a given object into its string representation.
m = 1e4 #m is a float, a number that can have a decimal point. It was written in scientific notation.

       # Questions
       # 1. I found 9 different data types.
       # 2. integer, float, string, complex number, list, dictionary, tuple, Boolean, None
       # 3. a and b; d and l; e, h, and k
       # 4. l was a string, because the str() function was used to convert it from an integer to a string

n = range(5) # n is a range, which is an immutable sequence of numbers often used in loops.
print(n)
print(type(n))

# --- Booleans ---
print(10>9) #True because 10 is greater than 9 
print(10==9) #False because 10 doesn't equal 9
print(10<=9) #False because 10 isn't less than or equal to 9
print(bool("abc")) #True because of the "truthiness" of the object
print(bool(123)) #True because of the "truthiness" of the object
print(bool(["apple", "cherry", "banana"])) #True because of the "truthiness" of the object
print(bool(True)) #True because of the (obvious) truthiness of the object
print(bool(False)) #False because it is the Boolean value False
print(bool(0)) #False because 0 is a "falsy" value
print(bool("")) #False because an empty string is a "falsy" value
print(bool(" ")) #True because of the "truthiness" of the value. This string isn't empty, it contains a space.
print(bool(())) #False because an empty tuple is a falsy value
print(bool([])) #False because an empty list is a falsy value
print(bool({})) #False because an empty dictionary is a falsy value
print(bool(True and False)) #False because one of the operands is false
print(bool(True and True)) #True because both operands are true
print(bool(False and False)) #False because the operands are false
print(bool(True or False)) #True because the or operator evaluates to true if at least one operand is true
print(bool(True or True)) #True because both operands are true
print(bool(False or False)) #False because both operands are false
print(bool(not(False))) #True because "not False" means it's the only other option, which is true
print(bool(not(True))) #False because "not True" means it's the only other option, whcih is false

#Questions
# 1. True or False doesn't necessarily only apply to numbers. The objects have a quality of "truthiness" to them, which I interpret to mean that it is what it's supposed to be? And when there's nothing there, it returns False.
# 2. The expressions with "and" and "or" operators surprised me because they follow a slightly different pattern than the others.
# 3. 
print(bool("My name is Nandini"))
#This expression will return True because it is a string with content in it and is a "truthy" value
# 4. 
print(7+9 > 100)
#This expression will return False because 7 + 9 < 100.

# --- Operators ---
#Arithmetic operators
10 + 5 #15, addition
10 - 5 #5, subtraction
2*4 #8, multiplication
6/3 #2, division
5 % 2 #1, the remainder of 5 divided by 2
3 ** 2 #9, squared the first number
15 // 2 #7, did 15 divided by 2 and then rounded down to the nearest integer.

#Comparison operators
5 == 2 #false, it asks if 5 equals 2
10 != 10 #false, it asks if 10 does not equal 10
2 < 5 #true, it asks if 2 is less than 5
12 > 5 #true, it asks if 12 is greater than 5
5 <= 6 #true, it asks if 5 is less than or equal to 6
1 >= 10 #false, it asks if 1 is greater than or equal to 10

#Assignments Operators
x = 5
x += 5 #adds 5 to x, reassigns variable
x -=4 #subtracts 4 from x, reassigns variable
x *= 3 #multiplies 3 by x, reassigns variable
print(x)

#Logical operators
#1: the operator and returns true if both conditions on the left and right are true, and if not it returns False
True and True
False and True
#2: the operator or returns True if at least one condition is true, and false only if both are false
True or False
False or False
#3: the operator not returns the opposite of the object's Boolean value
not True
not False

#More questions
#1: / does regular division, // does floor division (rounding down to the nearest whole number)
#2: % does division and returns a remainder, // does floor division
#3: %
10 % 3
#4: they assign a value to a variable

# --- Strings ---
my_string = "hello"
print(my_string)
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[-1])
print(my_string[1:3])
print(my_string[0:5:2])
print(len(my_string))
print(my_string + "goodbye")
print(7*my_string)

#Questions
#1. slicing is used to extand a portion of a string, list or tuple. the format is sequence[start:stop:step]. I sliced it for 8 and 9.
#2. it prints "Hello, my name is Oski"
name = "Oski"
print("Hello, my name is", name)
#3. it prints the same thing as the previous
name = "Oski"
print(f"Hello, my name is {name}")
#4. it printed the same thing, but f-strings help embed expressions or variables within strings more easily.

# --- Terminal Commands ---
#1. cd stands for "change directory", it helps move from one directory to another
#2. ls stands for list, and displays the contents of a directory
#3. ls -a lists all files and directories, including hidden ones
#4. mkdir "make directory", makes a new directory
#5. cat "concatenate" prints the entire content of a file onto the terminal screen
#6. pwd "print working directory" shows the pathway to get to the directory you're  in
#7. cd .. navigates one level up in the directory hierarchy 
#8. cd . navigates to the directory you're currently in
#9. cd ∼ changes the current working directory to the home directory for the user
#10. cp copies files and directories to a new destination
#11. mv moves or renames files and directories
#12. rm (be careful with this one) removes files or directories
#13. clear removes all previous output, so you're back to a blank window. ctrl+L does the same thing but it still lets you scroll back up to see previous content
#14. grep helps you search for specific lines of text/pattern in a file

#Questions
#1. uniq reports or omits repeated lines, wc counts lines, words, and characters in a file, netstat displays network connections
#2. ls -a also shows hidden files, while ls doesn't
#3. a file that isn't displayed by default in a file explorer, so that you don't accidentally delete or modify it
#4. -v increases the level of detail in output, -q suppresses nonessential output, -f overrides prompts/warnings and proceeds with an action
