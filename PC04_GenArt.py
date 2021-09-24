"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Kaily Fox

********* HEY, READ THIS FIRST **********

My image is of a star and a moon in the night sky. I decided to do this 
because the sky is one of my favorite parts of nature. Its' beauty is so 
simplistic yet breath taking. The natural phenomenas that occur in the sky 
never fail to amaze and calm me. 

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
#set up star turtle 




star = turtle.Turtle()
star.up()
star.speed(10)
star.goto(random.randint(-150,150),random.randint(-150,150))
star.color("yellow")
star.pensize(8)
star.begin_fill()
star.down()

#create loop for star
numInt=int(15)
for i in range(numInt):
    star.forward(100)
    star.right(144)
star.end_fill()
star.up()

#set up moon turtle
moon = turtle.Turtle()
moon.up()
moon.goto(random.randint(-150,150),random.randint(-150,150))
moon.color("grey")
moon.pensize(15)
moon.down()
moon.begin_fill()
moon.circle(20)
moon.end_fill()
moon.up()

#create craters for moon
moon.forward(20)
moon.down()
moon.color("white")
moon.pensize(2)
moon.begin_fill()

#create loop for craters
numInt=int(4)
for i in range(numInt):
    moon.circle(3)
    moon.up()
    moon.forward(5)
    moon.right(5)
moon.end_fill()

turtle.done() 

    




# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()





 
