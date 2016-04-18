Functions: A named sequence of instructions. Functions abstract computer programs!
    result = function_name(parameters)
By making our own functions we can:
    Easily reuse algorithms (write less code!)
    Test and debug one piece of a program at a time
    Abstract an algorithm to focus on the bigger picture

Defining a Function: 
# general syntax
def function_name(params):
    statements
params are optional! comma-separated

def say_hello(name):
    print("Hello "+name)
    print("Nice to meet you!")
def say_hello(name):
    print("Hello "+name)
    print("Nice to meet you!")

say_hello("Joel")
say_hello("Class")
say_hello("Dave")

def download_html():
    #...

def extract_links():
    #...

def make_markdown():
    #...

def make_urls_absolute():
    #...

#write the script!
download_html()
extract_links()
make_markdown()
make_urls_absolute()

# "helper" functions
def download_html(url):
    #...
def extract_links(html):
    #...
def make_markdown(links):
    #...
def make_urls_absolute(markdown):
    #...

#function to get links as markdown. work at higher level of abstraction
def md_links(url):
    html = download_html(url) #call other methods
    links = extract_links(html)
    markdown = make_markdown(links)
    markdown = make_urls_absolute(markdown)

#just do the work!
md_links("https://ischool.uw.edu/")

Functions and Logic: 
def say_hello(name):
    if name.lower() == "dave":
        print("Dave's not here man")
    else:
        print("Hello "+name)
        print("Nice to meet you!")
# if make variable: my_name = "joel" --> say_hello(my_name)
say_hello("Joel")
say_hello("Class")
say_hello("Dave")

def draw(jeeves, value):
    if value == value_1:
        jeeves.fillcolor("")
    elif value == value_2:
        jeeves.fillcolor("")
    elif value == value_3:
        jeeves.fillcolor("")
    elif value == value_4:
        jeeves.fillcolor("")

Parameters are local variables that are assigned values when the function is called.
def say_hello(name):
    print("Hello "+name)
# (name="Joel" #implicit)

say_hello("Joel")

Scope: Variables are only available within the function in which they are defined. These are called local variables
(c.f. global variables which are available everywhere)
def sleep_in():
    wake_time = "after 7am"

print(wake_time) #error! 
                 #only available in 
                 #the function!

Local vs. Global: Local variables and global variables can have the same name (because at different scope). But they are still separate variables.
name = "Alice" # global variable 'name'

def say_hello(name): #local variable 'name'
    name = name #assign to self (redundant)
    print("Hi "+name) #using local variable

say_hello("Bob") #param assigned to local var

print(name) #using global variable

Function Parameters: Different functions can use the same name for their local variables.
!Just because local variables share a name doesnt mean they are the same!
def say_hello(name):
    print("Hello "+name)

def say_goodbye(name):
    print("Bye "+name)

say_hello("Alice")
say_goodbye("Bob")

Return Values: Functions can also produce (return) a result. This is different than printing an output.
def square(number):
    result = number*number
    return result # if didnt have "return", would not produce a result that you can keep track of and use later (is not printed/visible --> stores for compy to use later)

def triple(number):
    return number*3

#remember to give the result a label!
x2 = square(6)
x3 = triple(8)
# print(x2)
# print(x3)

Returned values are like function output for the computer; printed output is for the human
def square(number):
    result = number*number
    print(result) #output for human
    return result #output for computer


def say_hello(name):
    print("Hello "+name)

greeting = say_hello(name)
print(greeting) #None! No returned value
                #that a computer could remember

def square(number):
    result = number*number
    print(result) #output for human
    return result #output for computer

x2 = square(6)

answer = square(3)+square(4)
print(answer) #prints out x2, square(3), square(4), and answer (demonstrates why we dont typically print when want return)

Function Practice: Turn the compound interest algorithm in interest.py into a function called calculate_interest()

Instead of prompting the user, it should take in the principle, rate, and time as parameters, and return the interest earned.
 
Bonus: call your function to demonstrate the validity of the Rule of 72

Iteration (loops): Doing the same thing over and over and over and over and
While Loop:
# general syntax
while boolean_expression:
    statements

count = 5 #declare variable
while count > 0: #check if conditional is true, if true, run indented statements, then go back to beginning and check again until count = 0 and conditional statement no longer true, so leaves loop and goes to print blastoff
    print(count)
    count = count - 1

print("Blastoff!")

What could go wrong?
count = 0 #we count from 0
while count < 100:
#while count == 100: #<-- count is not equal to 100, therefore is not going to go thru loop
#question is "should i keep going" NOT "am i there yet"
# while count != 100: #<--
    print(count)
    count = count + 1

while count != 100:
    print(count)
    count = count + 3 <-- infinite loop! therefore use inequalities (< >) for loops bc safer than !=

while count < 100:
    count = 0 <-- defining count before loop, cant determine what count is --> error
    print(count)
    count = count + 1

While Example:
# flip a coin until it shows up heads

import random # for random numbers

still_flipping = True # sentinel: guard telling you whether allowed to leave loop or not (store var that keeps track of whether we are still flipping)
while still_flipping:
    flip = random.randint(0,1) # pick a random int bt 0 & 1
    if flip == 0:
        flip = "Heads" # flip is now a string
    else:
        flip = "Tails"
    print(flip)
    if flip == "Heads":
        still_flipping = False # change state to false, close loop
    # Modify to flip until you get two heads in a row!

Input Validation:
# returns a user-inputted number between
# min and max
def input_number(min, max):
    valid = False
    while(not valid):
        number = int(input("Pick a # between "+str(min)+" and "+str(max)+": "))
        if(min <= number <= max):
            valid = True
        else:
            print("Invalid number")
    return number

#call function and print result
print(input_number(1,5))

For Loop: 
for count in range(100):
    print(count)

Range: Represents a sequence of numbers (https://docs.python.org/3/library/stdtypes.html#ranges)
# python data strx range(min, max, count)
# always start from 0 unless otherwise specified (i.e. with negative number as min)
# numbers: 0 through 9 # always start counting at 0!
# (aka 0 to 10, not inclusive)
range(10) 

# 1 through 11 (not inclusive)
range(1,11) 

# numbers: 0, 3, 6, 9
# (0 through 10, not inclusive,
# skipping by 3)
range(0, 10, 3)

list(range(5))
--> [0, 1, 2, 3, 4]

For Loop: Executes statements once for each item in the collection. The item is assigned to the local variable (e.g., local_var). Goes thru a list and goes thru statement for every item in that list.
#general syntax
for local_var in collection: 
    statements
for each item im calling local_var thats in the collection, do stuff
# take each item in list (local cllxn) and assign it to a local var
local_var=item #implicit


While Loops: Indefinite Iteration
    When you dont know how many times youll go through the loop until youre in it (e.g., coin flipping).
For Loops: Definite Iteration
    When you know how many times youll go through the loop ahead of time (e.g., counting). Even if the number of iterations is a variable.
All iteration can be written with a while loop

for count in range (5):
    print(5 - count)
    # 5-0, 5-1, 5-2, 5-3, 5-4
print("Blastoff! ZOOM!")

Lists: A mutable sequence of values. (https://docs.python.org/3/library/stdtypes.html#lists)
names = ["John", "Paul", "George", "Ringo"]

for name in names:
    print("Hello "+name)

Lists of Strings: We can get lists from strings using the split method.
line = "To be or not to be"
words = line.split() #split on \w+

for word in words:
    print(word)

Strings: Strings can be treated as a list of letters.
line = "To be or not to be"

for letter in line:
    print(letter)

Files: Files can be treated as lists of lines.
# "open" the file
# getting a reference to it
file = open('myfile.txt') #relative path

for line in file:
    print(line)

What could go wrong?
filename = input("File to open: ")

# "open" the file
file = open(filename)

for line in file:
    print(line)

Try/Except: A "conditional" block to check for errors. If an error occurs within the try block, the code inside the except block is immediately run before the script continues.
filename = input("File to open: ")

try: #this might break (not our fault)
    file = open(filename)
except: #catching FileNotFoundError
    print("No such file")

for line in file:
    print(line

Writing to File
# "open" the file with "write" access
file = open('myfile.txt', 'w')

file.write("Hello world!\n")
file.write("It's a mighty fine morning\n")

#note: write() does not include \n

How many lines?
file = open('words.txt')

count = 0
for line in file:
    count = count + 1

print(count, "words")

How many words?
file = open('book.txt')

count = 0
for line in file:
    words = line.split(' ') #space delimiter
    for word in words: # NESTED LOOP
        count = count + 1

print(count, "words")

How many words?
import re #for regex
file = open('book.txt')

count = 0
for line in file:
    # split on regex (not word or ' chars)
    words = re.split("[^\w']+", line)
    for word in words:
      if word != '':
        #print(word)
        count = count + 1

print(count, "words")

Average letters per line?
file = open('words.txt')

total_ltr = 0
count = 0
for line in file:
    total_ltr = total_ltr + len(line)
    count = count + 1

avg_len = total_letters/count

print("Average word length:", avg_len)

Does it contain a word?
file = open('words.txt')

target = input("Word to find: ")

found = False
for line in file:
    if line == target:
        found = True
    # NO ELSE

if found:
    print(target + " is in the list!")