
#                                   PYTHON

'''
This is my tutorial/referencebook that I will write in to explain/give examples
for everything I have learnt in python and coding so I can re-learn anything
if I forget or if someone else would like to learn some Python.
'''
"""
If Zed Shaw's "Learn Python the hard way" was the hard way, this is like that but the harder way because I'm not as good at explaining things.
No I didn't just copy this from that book, I actually got that book only after I wrote this. It was mostly written off an amalgamation of youtube videos and obscure
websites.
"""
'''
Feel completely free to make your own comments, re-write explanations and otherwise personalise it and maybe contribute new parts to it.
'''


#Started by Boyd Kirkman, 2016
#Further scrawled on by <enter your name and year here :)>

#IMPORTANT NOTE:
#This was written in python 2.7 so some things have probably changed - Boyd from the future of 2020
#On an unrelated note, the previous note, whilst written in 2020, was actually written pre-covid - Boyd from the future future of 2021
#On a more related note, the main difference from 2.7 to python 3 is that the print funtion MUST have brackets e.g. print("string") - Boyd from the slightly more futurey future of later in 2021

#If a program gets out of control always remember that Ctrl+C will stop it.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#COMMENTS

#this is a single line comment.
'''
This
is
a
multiple line
comment.
'''
"""
multiple line comments can also use 3 " or 3 '.
"""
#I will be using multiple comments throughout this... book?
#comments don't print out when the program is run.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#PRINT FUNCTION

'''
print can be used to create text and display certain things in the
shell an example of all the functions and things used in print:
'''
print 'hello'+' give me a high',5,str(6)
#there is aslo this, couldn't run it properly if it were in the above line.
print int(5)+float(8.5)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#MATH FUNCTION

'''
The math function is used in the shell just by typing the sum, though to use it
in a program like this one, you need to print it e.g. print(5+6) or
print(float(7.5)+9)
'''
# + = plus
# - = minus
# * = multiplication
# / = division
# to do 'to the power of' use two **
print 5+float(7.5)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#VARIABLES FUNCTION

'''
Variables act as a place holder for something else, e.g. numbers, math, etc.
you make a variable by simply typing the new name of the variable adding an
equals sign then the thing you are making a variable of.
'''
#An example of making a variable would be:
Example_Var = 55+94
#Now if you type out print(Example_Var) then run the program it would print out the sum of 55+94.
print Example_Var
'''
Now we will learn about packaging, packaging is were you create multiple
variables in a list (most cammonly co-ordinates), for this to work you have
to have the same amount of things listed on each side, the variables connect via
the order they are in.
'''
#An example of packaging would be:
x,y = (3,5)
#Now x = 3 and y = 5 so if we...
print x
#It will print 3 and if we...
print y
#It will print 5



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#LOOPING

'''
There is two ways to loop, using the while function and using the for function.
Both the while loop and the for loop are similar and can both be used to
do the same things. Using either really just comes down to personal preferance.
'''

#THE WHILE LOOP

'''
The while loop loop is used to perform an operation while under a conditon
(which is what ever you set). It is mainly used for counting.
'''
#An example of a while loop looks like this:
condition = 1

while condition < 11:
    print condition
    condition += 1
#condition += 1 is really the same as condition = condition + 1
#All it is doing is permanently adding 1 to the condition variable.
#You can also replace the < with >, ==(equalls), <=, >=, !=(doesn't equall)
'''
what is happening here is, I am making a variable called condition to represent
1, then whilst the condition is less than 10 it will print the condition then
permanently add 1 to the condition so that when the condition equals 11 or is
greater than 11, it will stop the loop. Overall, all it is doing is printing
the numbers 1 through to 10.
'''
"""
If you want create an infinite loop just type 'while true:' then what ever
operation you want it to perform. If it gets out of hand then hold control
and press c to cut the program and stop it from running. There won't be an
example for this one for obvious reasons.
"""

#THE FOR LOOP

'''
The for loop is usually used for more variable situations,also more commonly
used to go through a list.
'''
#An example of the for loop would be this:
Example_List = [1,2,5,9,88,5423,9987,6,9780]

for Each_Number in Example_List:
    print Each_Number,'elephants'
'''
What I have done is created a variable called Example_List that is a
list (obviously), then using the for and in statements, I have created a
variable that is each step of the list in Example_List. I have then made it
print each number in the list along with the word elephants. Overall, all the
basic operation it is doing is printing the list.
'''
#Other than listing, it is also a quicker way to count as it only uses 2 lines.
#To count it uses a fuction called range. e.g.
for x in range(1,11):
    print x
'''
What I have done is created a variable for every number in a range from 1 to 11
then printed out the list it has created.
'''



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#THE IF STATEMENT

'''
The if statement is used to check if something is the case and if it is the case
then do something, where as if it is not the case, do nothing and continue on with
the program.
'''
#An example of this would be:
x,y = 3,7

if x < y:
    print 'yay'
'''
What is happening is I am creating two variables to represent 3 and 7 then I
have made an if statement to say that if x < y which it is, then it will print
yay.
'''



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#THE ELSE STATEMENT

'''
The else statement is used with the if statement so that when the if statement
is not the case, instead of moving on with the program it will do something
else.
'''
#An example of this would be:
x = 6
y = 7

if x > y:
    print 'You shouldn\'t be reading this' #The \ before the ' ensures the interpreter doesn't read the ' as the end of the string
else:
    print 'You should read this'
'''
As you may have noticed, all I have done is add an else, then an operation, to
the end of the if statement. It should print the second print as x is not
greater then y.
'''



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#THE ELIF STATEMENT

'''
The elif statement or 'else, if' is used as (you guessed it) both an else and an
if statement at the sametime. It is used when making a chunk of if statements
and you want it to stop running through the if statements when one of the
statements is true.
'''
#In use it would look something like this:
x = 4
y = 6
z = 9

if x > y:
    print 'This is not the one'
elif x > z:
    print 'Neither is this'
elif x == 4:
    print 'This is the one'
elif y == 6:
    print 'This is true though will not run because the one before was true'
else:
    print 'This does nothing'
#As you can see, the elif acts exactly like an if statement.
#Though it only runs the first if statement that it finds is true.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#FUNCTIONS

'''
Functions are used to assign a set of code and possibly variables, known as
parameters, to a simple line of text.
'''
#An example would be
def example():
    print 'This is a function'
    x = 5+4
    print x

example()
'''
To start the function I had to define it so I use def then the new name followed
by two brackets then a colon. After that you type the lines of code you want the
function to perform then to make the function run you type out the functions
name followed by two brackets.
'''

#PARAMETERS

'''
The parameters are variables created for the function to work in certain
situations when needed.
'''
#An example of this would be when making a simple calculating function:
def Simple_Addition(num1, num2):
    answer = num1+num2
    print "The answer is",answer

Simple_Addition(5,7)
#The parameters are in the brackets after the naming of the function.
#This piece of code will be adding 5 and 7.

#DEFAULT FUNCTION PARAMETERS
'''
Defult function parameters automaticaly set a parameter to a value without you
having to type in a value for it.
'''
#An example would be:
def Default_Parameters(num1=7,num2=5):
    print num1,num2

Default_Parameters()
#Now num1 will default to 7 and num2 will default to 5.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#GLOBAL AND LOCAL VARIABLES

'''
Global variables are able to be accessed anywhere, Though a Local variable can
only be accessed in it's local area or frame.
'''
#An example would be:
x = 5
def Global():
    global x
    print x
    x+=3
    print x

Global()
'''
What I have done is made a variable, created a function, then in the function
made x a global variable, meaning I can modify it anywhere e.g. me adding
3 to x in the function. Using global and then the variable name can also be used
to create a global variable inside of a funtion as if the variable doesn't exist
it will just create a global variable called the thing you typed after global.
e.g. global x would create a global variable called x.
'''
#If you aren't allowed to use the global function, a way to do it would be:
x = 5
def Global_Two():
    globx = x
    print(globx)
    globx+=3
    print globx
    return globx

Global_Two()
print x
'''
This creates a new variable in the function that is the same as x, then once the
function is done it returns globx to x.
'''



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#TYPED INPUT
'''
There are two different functions for dealing with typed input, input() and
raw_input().
input() -> interprets the input text e.g. funtions typed will be recocgnised
           and ordinary text such as sentences will not be recognised and so
           will return an error.
raw_input() -> doesn't interpret what is wrighten and instead automatically
           treats it as a string.
'''
#An example of it in use would be:
name = raw_input("what's you're name? ")
print "Nice to meet you",name,"!"



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#Random Function
'''
To get started using Random, you must first import it
'''
import random

#A Random Word/Number From A List
'''
When you want to choose a random word from a list you must first dreate the
list as a variable, and then when calling to choose a random word from the list
you must use random.choice([INSERT VARIABLE NAME HERE]). An example of printing
a random word form a list can be seen below:
'''
a = ["three","random","words"]
print(random.choice(a))

#A Random Number From A Range
'''
This method will select a random number from the defined range, but remember
when you continue programing that it will be treated as an integer and not a
string. Instead of using random.choice() you use:
random.randint([INSERT MIN. NUMBER HERE], [INSERT MAX NUMBER HERE]).
An example of printing a random number from 1-10 can be seen below:
'''
print(random.randint(1,10))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#Arrays and Matrices
'''
Arrays and matrices are essentially a way of categorising data, with an array
being more single dimensional and a matrix being more two dimensional. It is
imporant to remember that when talking about matrices that their width and
height are listed as height then width e.g. 2 x 4
When making an array or matrix you will be using the numpy function so to begin
you must first import it.
'''
import numpy as np

#When using the numpy funtion there are many key functions within it.
#These include:
#Array
np.array([1,2,3,4])
#Random which is essentialy the same as the other random funtion
print np.random.choice(("HI","World"))
'''
Zeros could be used if you want to create an matrix of zeros, the two numbers
are the dimensions of the matrix. You can also use other terms such as ones to
make a matrix/array of ones etc.
'''
print np.zeros((3,2))



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#Operating commands using python!
'''
When using python you may find that you may need to use a command in the
terminal to accomplish ceratin tasks, for example clearing previous text in a
text based game. To import it use import os, then when you want to execute a
command use os.system("[Insert Command Here]") e.g.
'''
import os
os.system("clear")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DEBUGGING

#Some common errors include:
'''
Name Error: name 'name' is not defined - This means there is a typo in  your
variable naming or use of the variable that, in this case, is called name.
'''
"""
Expected an indented block - This means you have not entered anything in the
indentation where it would normaly require and indentation e.g not having
anything indented after, def Function(): .
"""
'''
Invalid Syntax - Can mean multiple things though usually means you didn't close
something off like the brackets of a function.
'''
"""
EOL while scanning string literal - This means that you havent closed off a
string of text.
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Using Pygame
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



'''
Pygame is a common way of creating simple games and visual programs in python.
'''



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#STARTING OFF

#To start off with using pygame first you must import it.
import pygame

#Next you must set some global variables for the height and width of the window.
#This also helps later on as, if you want to change the values it is much easier.
width = 640
height = 480
"""
After setting the global variables for the height and width go ahead and set
some more for other aspects that you would use e.g. radius of a circle,
stroke thickness, etc.
"""
radius = 100
stroke = 1

#Then with that out of the way you must initiate the pygame function.
pygame.init()

#Setting up the window, also called a pygame Surface object, a space to draw on.
'''
First set a global variable to call upon the command that sets up the
area in wich you can draw.
'''
window = pygame.display.set_mode((width,height))
"""
Then If you want to set up the window with a solid colour type the following:
"""
window.fill(pygame.Color(255,255,255))
'''
This fills the widow with white, the three numbers indicate the RGB values mixed
to create the background colours. Also remeber that Python was made by Americans
and Americans can't spell properly so words like colour are spelt color etc.
'''

#setup an infinite loop for the things you want to draw:
while True:
    #e.g. to draw a circle:
    pygame.draw.circle(window,
                       pygame.Color(255,0,0),
                       (width/2,height/2),
                       radius,
                       stroke)
    pygame.display.update()
"""
To make it show up you need to update the surface by either using update()
or flip():
"""
#From my personal expirience update() refreshes the surface faster and smoother.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#HANDLING THE EVENT OF A KEY PRESS/MOUSE CLICK IN PYGAME

#A Key Press:
if pygame.key.get_pressed()[pygame.K_b]:
    pass
else:
    pass
'''
This little piece of code does nothing, it just shows the layout of what you
need to type when you want to handle the event of a keypress. For each key
you type the same pygame.key.get_pressed()[] but in the [] you type the name
of each key. A handy list of all the keys can be found in the following link;
https://www.pygame.org/docs/ref/key.html
'''
