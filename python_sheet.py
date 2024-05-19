
#################################	
## Main Python Data Types
#################################	
# Every value in Python is called an "object". And every object has a specific data type. 
# The three most-used data types are as follows:

-2, -1, 0, 1, 2, 3, 4, 5   # Integers (int)

-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25    # Floating-point numbers (float)

# The following are considered False
    # None
    # False
    # zero of any numeric type, for example, 0, 0.0
    # any empty sequence, for example, '', (), [].
    # any empty mapping, for example, {}.

 'yo', 'hey', 'Hello!', 'what' # Strings
# In Python 3, strings are immutable. If you already defined one, you cannot change it later on.
# While you can modify a string with commands such as replace() or join(), 
# they will create a copy of a string and apply modification to it, rather than rewrite the original one.

# raw string 
# to have string without any special characters
raw = r"I wouldn\t escape this\n."
print(raw) # I wouldn\t escape this\n.

# string rules
# 1- You can create a string in three ways using single, double or triple quotes. 
# 2- Whichever option you choose, you should stick to it and use it consistently within your program.
# 3- String Concatenation --> to add two strings together using the "+" operator.
string_three = string_one + string_two 
# 4- You can't apply + operator to two different data types e.g. string + integer.
# 5- String Replication
print("Alice" * 5)	# prints 'AliceAliceAliceAliceAlice'
# 6- can apply string concatination with \ or '''
crossLine1 = "This spans" + \
"a code line"
crossLine2 = \
"""
This string is designed to span
lines and be exactly as you see
it (including line breaks)
"""

# some string functions
upper()
lower()
find()
index()
isalnum()
isalpha()
isnumeric()

# string format 
"Hello {0}, today is {1}. Right {0}?".format("Michael", "Monday") # Hello Michael, today is Monday. Right Michael?
"{0:,} is pretty big!".format(1234567890) # 1,234,567,890 is pretty big!
"You can name your args {jeff} and {tony}!".format(jeff="bigj", tony="t-boy")

# advanced target multiple items in array with format 
# n is array of numbers with many items
"({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# They can be combined via + or just adjacency
"Combine " + "this" # "Combine this"
"Combine " "this" # "Combine this"


#################################	
## Math Operators
#################################	
**	Exponent	        # 2 ** 3 = 8
%	Modulus/Remainder	# 22	% 8 = 6
//	Integer division	# 22	// 8 = 2
/	Division	        # 22	/ 8 = 2.75
*	Multiplication	    # 3	*	3	=	9
-	Subtraction	        # 5	-	2	=	3
+	Addition	        # 2	+	2	=	4
 
#################################	
## Built-in Functions in Python
#################################	
print()
print(a, b, c) # prints each variable in new line
input() # prompt the user for some input - All user input is stored as a string.
    age = input("How old are you")
    print("So, you are already " + str(age) + " years old, ")

len() # to find the length of any string, list, tuple, dictionary, or another data type. 
print("The length of the string is :", len(str1))

filter() # to exclude items in an iterable object (lists, tuples, dictionaries, etc)
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
    if x < 18:
        return False
    else:
        return True
adults = filter(myFunc, ages)

 
#################################	
## How to Define a Function
#################################	

name.py
def name():
    print("What’s your name?")
name()
 
# A function can also accept keyword arguments. 
# In this case, you can use parameters in random order 
# as the Python interpreter will use the provided keywords
def product_info(product name, price):
    print("productname: " + product name)
    print("Price " + str(price))
# Call function with parameters assigned as above
product_info("White T-shirt", 15)
# Call function with keyword arguments
product_info(productname="jeans", price=45)

# Variables initialized within a function are scoped to that function
# function can return multiple values
def findUserInfo(userId):
    user = db.find(userId)
    return user.email, user.name
email, userName = findUserInfo(42)

# global keyword can promote scope
sharedVal = 3
def method1():
    global sharedVal
    if sharedVal == 3:
        sharedVal = 7

# function can be passed as a parameter
def strategyMethod(num, predicate):
    if predicate(num):
        print('would perform action')
    else:
        print('not happening!')
def isByThree(num):
    return num % 3 == 0
strategyMethod(6, isByThree)

# function can accept tuble
def positional(x, y, *args):
    print(x, y, args)
positional(1, 2, 6, 7, 8) # prints 1 2 (6, 7, 8)

# function can accept dictionary
def keywordArguments(x, y, **kwargs):
    print(x, y, kwargs)
keywordArguments(1, 2, z=2, u=1, mode="reversed") # prints 1 2 {'u': 1, 'z': 2, 'mode': 'reversed'}

# call function with it's string name
getattr("class_name", "function name")()

# create object with class string name
globals()["class_name"]()

#################################	
## Higher Order Functions
#################################
# A Function that contains other functions as a parameter or returns a function as an output

## map function
## executes a specified function for each item in an iterable.
def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))

# map(function, iterables , iterables)
def myfunc(a, b):
  return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

## filter function
## returns an iterator where the items are filtered through a function to test if the item is accepted or not.
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)

## reduce function (aggregate function)
## used to apply a particular function passed in its argument to all of the list elements
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result 
# and the number just succeeding the second element and the result is again stored.

# importing functools for reduce() 
import functools 
  
# initializing list 
lis = [1, 3, 5, 6, 2] 
  
# using reduce to compute sum of list 
print("The sum of the list elements is : ", end="") 
print(functools.reduce(lambda a, b: a+b, lis)) 
  
# using reduce to compute maximum element from list 
print("The maximum element of the list is : ", end="") 
print(functools.reduce(lambda a, b: a if a > b else b, lis)) 

#################################	
## Lists
#################################	
# Lists are another cornerstone data type in Python 
# used to specify an ordered sequence of elements. Unlike strings, lists are mutable (=changeable).
# Each value inside a list is called an item and these are placed between square brackets.
# Example lists
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["4", d, "book", 5]
# Alternatively, you can use list() function to do the same:
alpha_list = list(("1", "2", "3"))
print(alpha_list)

# to access last element - index backward
Last = beta_list[-1]

# add at the end of list 
beta_list.append("grape")

# add at specific index
beta_list.insert("2 grape")

# remove specific item
beta_list.remove("apple")

# remove last item
beta_list.pop()

# remove specific index
del beta_list [1]

# Combine Two Lists
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
combo_list = my_list + my_list2
combo_list
[1, 2, 3, 'a', 'b', 'c']

# can use extend to combine two lists
num.extend([23,97])

# Create a Nested List
my_nested_list = [my_list, my_list2]
my_nested_list
[[1, 2, 3], ['a', 'b', 'c']]

# Sort a List
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
alpha_list
[2, 23, 34, 67, 88, 100]

# Slice a List
alpha_list[0:4]
[2, 23, 34, 67]

num = [7, 11, 13, 17, 19]
num[2:4] # [13, 17]
num[2:] # [13, 17, 19] omit end index = len(num)-1
num[:3] # [ 7, 11, 13] omit start index = 0
num[-2:] # [17, 19] reverse

# Copy a List
beta_list = ["apple", "banana", "orange"]
beta_list = beta_list.copy()

# Alternatively, you can copy a list with the list() method:
beta_list = ["apple", "banana", "orange"]
beta_list = beta_list.copy()

# List  Comprehensions
list_variable = [x for x in iterable]	

# list comprehensions with two lists 
list_variable = [ x * y for x in vec1 for y in vec2 ]

# List comprehensions with if condition (ternary operator)
number_list = [x ** 2 for x in range(10) if x % 2 == 0]


#################################	
## Tuples
#################################	
# Tuples are similar to lists  However, they are immutable 
# you can't change the values stored in a tuple.
# The advantage of using tuples - slightly faster. So it's a nice way to optimize your code.
# How to Slide a Tuple - The process is similar to slicing lists.
my_tuple = (1, 2, 3, 4, 5)
my_tuple[0:3]
(1, 2, 3)

# Convert Tuple to a List
# Since Tuples are immutable, you can't change them. 
# What you can do though is convert a tuple into a list, 
# make an edit and then convert it back to a tuple.
x = ("apple", "orange", "pear")
y = list(x)
y[1] = "grape"
x = tuple(y)
print(x)

#################################	
## Dictionaries
#################################	
# A dictionary holds indexes with keys that are mapped to certain values. 
# to offer a great way of organizing and storing data in Python. 
# They are mutable, meaning you can change the stored information.
# A key value can be either a string, Boolean, or integer. 
Customer = {'username': 'john-sea', 'online': False, 'friends':100}

# How to Create a Python Dictionary
new_dict = {}
other_dict= dict()

# How to Access a Value in a Dictionary
x = new_dict["brand"]	
dict.keys() # isolates keys
dict.values() # isolates values
dict.items() # returns items in a list format of (key, value) tuple pairs

# Loop Through the Dictionary
#print all key names in the dictionary
for x in new_dict:
    print(x)
#print all values in the dictionary
for x in new_dict:
    print(new_dict[x])
#loop through both keys and values
for x, y in my_dict.items():
    print(x, y)

#################################	
## If Statements
#################################	
# Just like other programming languages, Python supports the basic logical conditions from math:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# If Statement Example
if 5 > 1:
    print("That’s True!")

# Nested If Statements
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else: ticket_price = 15

# If-Not-Statements
new_list = [1, 2, 3, 4]
x = 10
if x not in new_list:
    print("'x' isn’t on the list, so this is True!")

# Pass Statements - If statements can't be empty. But if that's your case, 
# add the pass statement to avoid having an error:
a = 33
b = 200
if b > a:
    pass

# ternary operator
name = "Jeff"
val = "short name" if len(name) < 5 else "long name"
print(val) # prints 'short name'

#################################	
## Python Loops 
#################################	

# For Loop
# loop through string
for x in "apple":
    print(x)

# while loop 
while i < 8:
    print(i)
    if i == 4:
        break
    i += 1

# All looping constructs support a final clause using else
# • Only runs if either
# – the loop completes without early breaks
# – the loop completes but never runs
while v < 10:
    v += 1
    print(v)
    if v == 9:
        break
else:
    print("else v is now " + str(v))

# When your scripts are imported, they may run code you did not
# intend to run
# – Use the __name__ convention to test if your script is the main script.
if __name__ == "__main__":
    #your code here

#################################	
## import
#################################	

import dmIO.names # default: keep namespace
from dmIO.names import queryUserForName # single method / class
from dmIO.names import * # import everything, no namespaces

#################################	
## Class
#################################	
# python doesn't support multiple constractors
# but you can pass default value if it's not passed
def __init__(self, city="Berlin"):
  self.city = city

# Python does not support function overloading. 
# When we define multiple functions with the same name, 
# the later one always overrides the prior and thus, in the namespace, 
# there will always be a single entry against each function name.

# How to Create a Class
class TestClass:
    z = 5

# How To Create an Object
p1 = TestClass()
print(p1.z)

# anther class example
class car(object):
    # constructor
    def __init__(self, color, doors, tires):
        self.color = color
        self.doors = doors
        self.tires = tires
    def brake(self):
        return "Braking"
    def drive(self):
        return "I’m driving!"
    # destructor
    def __del__(self):
        print("deleted, good bye " + self.name)

    # read only method
    @property # __name defined in __init__
    def name(self):
        return self.__name
    # setter method
    @name.setter
    def name(self, val):
        if len(val) > 0:
            val = val[0].upper() + val[1:]
            self.__name = val
    # static method
    @staticmethod
    def from_JSON(jsonText): # No self argument
        p = Person()
        # set values
        return p
# inheretance 
class Animal: # base class
    def __init__(self):
        print("creating animal")
class Cat(Animal): # cat is an animal
    def __init__(self, name, friskiness=50):
        super().__init__()
        self.name = name
        self.friskiness = friskiness
        print("creating cat" + name)

# How to Create a Subclass
class Car(Vehicle):
    def brake(self):
        # Override brake method
        return "The car class is breaking slowly!"

# print all vars
def printVars(self):
    attrs = vars(self)
    print(', '.join("%s: %s" % item for item in attrs.items()))
# Dealing with Python Exceptions (Errors)
# The Most Common Python Exceptions
AttributeError — pops up when an attribute reference or assignment fails.
IOError — emerges when some I/O operation (e.g. an open() function) fails for an I/O-related reason, e.g., "file not found" or "disk full".
ImportError — comes up when an import statement cannot locate the module definition. Also, when a from… import can't find a name that must be imported.
IndexError — emerges when a sequence subscript is out of range.
KeyError — raised when a dictionary key isn't found in the set of existing keys.
KeyboardInterrupt — lights up when the user hits the interrupt key (such as Control-C or Delete).
NameError — shows up when a local or global name can't be found. 
OSError — indicated a system-related error.
SyntaxError — pops up when a parser encounters a syntax error.
TypeError — comes up when an operation or function is applied to an object of inappropriate type.
ValueError — raised when a built-in operation/function gets an argument that has the right type but not an appropriate value, and the situation is not described by a more precise exception such as IndexError.
ZeroDivisionError — emerges when the second argument of a division or modulo operation is zero.

# How to Troubleshoot the Errors
# Python has a useful statement, design just for the purpose of handling exceptions —  try/except statement.
# Adding an else clause will help you confirm that no errors were found:
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other problem happened!")
else:
    print("No error occurred!")

try:
    u = find_user(11)
    u.registered = True
    save_user(u)
    fout.write("User updated")
except Exception as e:
    print("Error: " + str(e))
finally:
    fout.close()

# to throw error
# raise UserNotFoundError(userId)

# enums are defined as specialized classes
import enum
class DaysOfWeek(enum.Enum):
    sunday = 1
    monday = 2
    tuesday = 3
    wednesday = 4

day = DaysOfWeek.wednesday

#################################	
## date
#################################	

from datetime import date
from datetime import time
from datetime import datetime
today = date.today()
print("Today is {month}/{day}/{year}".format(month=today.month, day=today.day, year=today.year)) 

now = datetime.now()
print("Right now it's {0}h:{1}m:{2}.{3}sec".format(now.hour, now.minute, now.second,now.microsecond//1000))

# use timedelta calss for date operations
from datetime import timedelta
dt = timedelta(hours=1, minutes=5)
now = datetime.now()
later = now + dt

# date parsing
txt = "Monday, November 21, 2013"
day = datetime.strptime(txt, "%A, %B %d, %Y")
print(day) # 2013-11-21 00:00:00


#################################	
## files
#################################	

csvFileName = "SomeData.csv"
fin = open(csvFileName, 'r', encoding="utf-8")
lines = fin.readlines()
for line in fin:
    print(line, end='')

fin.close() # file should be closed after finished

# with keyword should close file automatically
csvFileName = "SomeData.csv"
with open(csvFileName, 'r', encoding="utf-8") as fin:
    for line in fin:
        print(line, end='')

# append string to file
fout.write("The application is starting up...\n")

# to read file in binary mode
bytes = bytearray()
with open(srcFile, 'rb') as fin:
    chunkSize = 1024
    buffer = fin.read(chunkSize)
    while buffer:
        bytes.extend(buffer)
        buffer = fin.read(chunkSize)

# xml
from xml.etree import ElementTree
xmlFile = "blog.rss.xml"
dom = ElementTree.parse(xmlFile) # load xml from a file
items = dom.findall('channel/item')
print("Found {0} blog entries.".format(len(items)))
entries = []
for item in items:
    title = item.find('title').text
    link = item.find('link').text
    entries.append( (title, link) )

# xml from string
xmlContent = "<rss><channel>...</channel></rss>"
dom = ElementTree.fromstring(xmlContent) # load xml from string

# json from string 
import json
jsonTxt = '{"name": "Jeff", "age": 24}'
d = json.loads(jsonTxt)

# json from dictionary 
d = dict(name="Jeff", age=24)
jsonTxt = json.dumps(d)

#################################	
## random
#################################	
import random
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# Random numbers depend on the seeding value. 
# if the seeding value is 5 then the output of the  program will always be the same.
print(random.random())

# return random integer
randint(start, end)

# get random number
random.random()

# shuffle list
random.shuffle(sequence, function)


#################################	
## lambda
#################################
# lambda is an inline function that have any number of inputs and one expression
x = lambda a, b : a * b
print(x(5, 6))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))


#################################	
## gui library
#################################
from tkinter import*
class TK_extended(Tk):
    def __init__(self, master , title):
        self.master = master
        self.title = title
    def create(self):
        self.master = Tk()
        self.master.title(self.title)
    def resize(self, width , height):
        self.master.geometry("{}x{}".format(width , height))
    def generate(self):
        self.master.mainloop()

root = TK_extended("win" , "My Window")
root.create()
root.resize(1000 , 300)
root.generate()


#################################	
## overloaden operator
#################################
class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)

print(ob1 + ob2)


#################################	
## run file direclty with arguments
#################################
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 5:
        print("xxx Error rquired 5 arguments")
    else:
        for item in sys.argv:
            print(item)


#################################	
## open your folder from browser localhost:8000
#################################
python3 -m http.server 8000


#################################	
## simple server code
#################################
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)
        # Setting the header
        self.send_header("Content-type", "text/html")
        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()
        # Extract query param
        name = 'World'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components["name"][0]
        # Some custom HTML code, possibly generated by another function
        html = f"<html><head></head><body><h1>Hello {name}!</h1></body></html>"
        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))
        return

# Create an object of the above class
handler_object = MyHttpRequestHandler
PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)
# Star the server
my_server.serve_forever()


