# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:02:54 2020

@author: Garret Bedford
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Garret Bedford
September 4, 2020

Draws a large triangle and a pair of red+blue glasses onto the photo.
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) 

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue")
panel.bgpic(image)

#=======Add your code here======
#first, change color and pick up turtle
color(70,102,255)
width(8)
up()

#drawing the triangle
goto(370,-150)
down()
goto(100,250) #turtle goes to each corner of the triangle
goto(-375,25)
goto(370,-150)
up()




#goto first glasses coordinate
#goto(-90,115)


#draw the glasses

lenses = [(-15,100), (40,110)] #contains the position of each lens


#draw the frame
color('black')
pensize(5)
goto(-100,120)
down()
goto(65,120)
up()




#draw the lenses

for i in lenses:
    goto(i)
    # these if statements decide what the color of the lens is based on the location of the turtle
    if i == (-15,100):
        color("blue")
        fillcolor("darkblue") 
    if i == (40,110):
        color("red")
        fillcolor("darkred")
    down()
    begin_fill()
    circle(16)
    end_fill()
    up()
    
    
done() #finish the drawing
    
    
    
    
    
#The code you had setup originally was pretty good. It did what it was supposed to do and it wasn't too difficult to figure out what exactly was happening by going through it.
#Most of the improvements I made were to streamline the code to do the same thing in less lines, and to make it a bit more clear what the code was doing.
#I think the only realy big problem with the original code was that it was all in this big block of text. I think it's easier to read through when the code is divided up into smaller pieces where it's completing different tasks. Just make sure the organization is easy to understand, and you're all set.
#Having seen your procedural art project, I can safely say that you've improved since this project. The code was already pretty good- it was a little clunky, but ultimately functional and organized well enough to be understood. All I have to say is keep up the good work!
    
    
