import turtle
import math
import random
import time

window = turtle.Screen()
window.screensize(1920,1080)
rr = 1920/1080
window.setup(width=1.0, height=1.0, startx=None, starty=None)

turtle.bgcolor('black')
turtle.hideturtle()
turtle.color('green')
turtle.tracer(2, 0)
time.sleep(5)

def triangle(t, side):
    
    for _ in range(3):
        t.forward(side)
        t.left(120)
    
    

l1 = 1
l2 = 1
# turtle.penup()
# turtle.goto(0,-100)
# turtle.pendown()
angle = 2
side = 10900
for i in range(0, 100):
    
    turtle.penup()
    turtle.home()
    side = side*0.95
    side_bar = side*math.sin(math.pi/3)*math.sqrt(2)/2
    x =   -math.cos(math.pi/6 + i*math.pi*angle/180)*side_bar
    y =  -100 -math.sin(math.pi/6 + i*math.pi*angle/180)*side_bar
    
    turtle.goto(x,y)
    #turtle.dot(10)
    turtle.left(angle*i)
    turtle.pendown()
    
    triangle(turtle, side)
    
    
    

turtle.mainloop()