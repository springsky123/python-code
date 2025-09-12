import turtle
t = turtle.Turtle()
t.speed(5)
turtle.bgcolor("lightblue")

directions = [("N",90,"red"),("E",0,"green"),("S",270,"blue"),("W",180,"orange")]

for label, angle, color in directions:
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.setheading(angle)
        t.forward(100)
        t.write(label, font = ("Arial",16,"bold"))
        t.backward(100)
turtle.done()
