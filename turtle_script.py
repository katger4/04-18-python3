# testing demo stuff can go here!

import turtle

def drawBar(t, height):
    if a == 48:
        t.fillcolor("red")
    elif a == 117:
        t.fillcolor("blue")
    elif a == 200:
        t.fillcolor("green")
    elif a == 240:
        t.fillcolor("yellow")
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape


# bar_color = ["red", "blue", "green", "yellow"]
xs = [48, 117, 200, 240]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
# tess.fillcolor(bar_color)
tess.pensize(3)



for a in xs:
    drawBar(tess, a)

wn.exitonclick()