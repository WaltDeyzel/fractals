import turtle
import random
import time
def branch(t, branchLength, shorten, angle):
      
  if branchLength > minLength:
    t.forward(branchLength)
    
    new_length = branchLength - shorten
   
    t.left(angle)
    branch(t, new_length, shorten, angle)
    t.right(angle * 2)
    branch(t, new_length, shorten, angle)
    t.left(angle)
    t.backward(branchLength)

def circleTrees(n):
 
  g = 360/n
  
  for i in range(n):
    tree.setheading(g*-i)
    branch(tree, 50, 7, 13)
    
if __name__ == "__main__":
  tree = turtle.Turtle()
    
  window = turtle.Screen()
  window.screensize(1920,1080)
  rr = 1920/1080
  window.setup(width=1.0, height=1.0, startx=None, starty=None)

  turtle.bgcolor('black')
  tree.hideturtle()
  tree.color('green')
  turtle.tracer(1, 0)
  time.sleep(5)
  
  minLength = 5
  
  circleTrees(3)
  
  # time.sleep(3)
  # minLength = 10 
  # tree.clear()
  # tree.setheading(90)
  # tree.penup()
  # tree.sety(-250)
  # tree.pendown()
  #branch(tree, 100, 10, 120)
    
  #tree.clear()
  
  #branch2(tree, l)
  
  turtle.mainloop()
  