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

tracer(5, 0)
n = 3 # number of points on circle
rad = 2*math.pi/n;

def draw(x, y, radius):
  penup()
  setx(x)
  sety(y)
  pendown()
  circle(radius)

def drawCircle(x,  y, radius): 
  
  draw(x, y, radius)
  
  if(radius > 10): 
    div = 2
    #print(x, y, radius)
    drawCircle(x + radius, y+radius/2, radius/div);
    drawCircle(x - radius, y+radius/2, radius/div);
    drawCircle(x, (y + radius*1.5), radius/div);
    drawCircle(x, (y - radius/2), radius/div);

def triCircle(x, y, radius):
      
      draw(x, y, radius);
    
      if(radius > 5):
        triCircle(x, y+radius*1.5, radius*0.5)
        triCircle(x-radius, y-math.sin(2*math.pi/3), radius*0.5)
        triCircle(x+radius, y-math.sin(2*math.pi/3), radius*0.5)

if __name__ == "__main__":
  #time.sleep(5)
  r = 500
  #triCircle(0, -350, r)
  drawCircle(0, -r, r)
  print('DONE')
  done()
