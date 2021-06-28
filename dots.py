from turtle import *
import math
import random
import time
color('green', 'yellow')
hideturtle()
bgcolor('black')
window = Screen()
window.screensize(1920,1080)
rr = 1920/1080
window.setup(width=1.0, height=1.0, startx=None, starty=None)
tracer(1, 0)
time.sleep(5)
n = 3 # number of points on circle
rad = 2*math.pi/n;
deg = rad*180/math.pi;
offset = math.pi/2

radius = 250;
div = 2
cords = [ ]

for i in range(n):
    
    x = radius*math.cos(rad*i + offset)
    y = radius*math.sin(rad*i + offset)
    cords.append((x, y))

for cor in cords:
    penup()
    setpos(cor)
    dot(5)

for _ in range(1000):
    
    newpos = random.choice(cords);
    x = (xcor() + newpos[0])/div
    y = (ycor() + newpos[1])/div
    setpos(x,y)
    dot(3)
done()