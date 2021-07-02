import turtle
import math
import random
import time

window = turtle.Screen()
window.screensize(1920,1080)
rr = 1920/1080
window.setup(width=1.0, height=1.0, startx=None, starty=None)

def settings(t):
   t.colormode(255)
   t.bgcolor('black')
   t.hideturtle()
   t.color('green')
   t.tracer(2, 0)
#time.sleep(5)

def go(t, x, y):
   t.penup()
   t.goto(x, y)
   t.pendown()

def goHome(t):
   t.penup()
   t.home()
   t.pendown()
   

# equilateral triangle
def triangle(t, side):
   for _ in range(3):
      t.forward(side)
      t.left(120)
      # t.dot(10)
       
def goldenTriangle(t, side_length, n):
   side = side_length
   angle = 1   
   for i in range(n):
      
      goHome(t)
      side = side*0.95
      side_bar = side*math.sin(math.pi/3)*math.sqrt(2)/2
      x =   -math.cos(math.pi/6 + i*math.pi*angle/180)*side_bar
      y =  -100 -math.sin(math.pi/6 + i*math.pi*angle/180)*side_bar

      go(t, x,y)
      t.left(angle*i)
      triangle(turtle, side)
      
def fibBlock(t, max_length, min_length):
   side_length_old = min_length
   side_length_new = min_length
   
   while side_length_old < max_length:
      t.forward(side_length_old)
      t.left(90)
      temp = side_length_new
      side_length_new = side_length_new + side_length_old
      side_length_old = temp
   goHome(t)

def goldenFibBlock(t, max_length, min_length, n, theta):
   angle = theta
   for i in range(n):
      fibBlock(t, max_length, min_length)
      t.left(angle*i)

def shape(t, n, radius, rad ,offset):
   
   cords = []

   for i in range(n):
    
      x = radius*math.cos(rad*i + offset)
      y = radius*math.sin(rad*i + offset)
      cords.append((x, y))
   
   t.penup()
   for cor in cords:
      t.setpos(cor)
      t.pendown()      
      t.dot(5)
   t.setpos(cords[0])

def universal(t, radius, n, a):   
   # N number of points 
   # angle between each dot 
   rad = 2*math.pi/n
   offset = math.pi/2
   
   
   for i in range(LOOP):
      t.left(a*i)
      fade(t, radius)
      shape(t, n, radius, rad, offset+a*i*math.pi/180)
      radius = radius*0.995
      goHome(t)

def fade(t, radius):
   # MUST MATCH RADIUS 
   R = 300
   f = 1
   shift = 90
   c = int(127.5*math.sin(radius*2*f*math.pi/R-shift*math.pi/180)+127.5)
   t.color(c, c, c)
   

if __name__ == "__main__":
   LOOP = 500
   # goldenTriangle(turtle, 1000, 100)
   # goldenSquare(turtle, 1300, 100)
   radius = 300
   settings(turtle)
   for i in range(1,5):
      settings(turtle)
      universal(turtle, radius, i, 0.05) # turtle, shape, degree ofset
      time.sleep(0.5)
      window.clearscreen()
      

