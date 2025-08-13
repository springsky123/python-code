#Turtle module

from turtle import *

colour = ['pink','purple']
speed(0)
bgcolor('black')
for i in range(16):
    for x in range(18):
        pencolor(colour[x%2])
        rt(90)
        circle(150-x*6,90)
        lt(90)
        circle(150-x*6,90)
        rt(180)
    circle(40,24)
done()
