import turtle
from turtle import *

turtle.title("CodeShow LapZ")
speed(15)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3:
        g+=2
    elif i<255*2//3:
        r-=2
    elif i<255:
        b+=2
    elif i<255*4//3:
        g-=2
    elif i<255*5//3:
        r+=2
    else:
        b-=2
    fd(20+i)
    rt(111)
    pencolor(r,g,b)

done()

