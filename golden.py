import turtle
import math
import random
import time

window = turtle.Screen()
window.screensize(1920,1080)
rr = 1920/1080
window.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.colormode(255)
turtle.bgcolor('black')
turtle.hideturtle()
turtle.color('green')
turtle.tracer(3, 0)
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
   

if __name__ == "__main__":
   
   goldenFibBlock(turtle, 800, 10, 170, 3)
   goldenTriangle(turtle, 1000, 100)

   time.sleep(3)

