from turtle import *

shape("turtle")
def draw_square():
   for i in range(4):
      forward(100)
      right(90)

for i in range(100):
   draw_square()
   right(5)

mainloop()