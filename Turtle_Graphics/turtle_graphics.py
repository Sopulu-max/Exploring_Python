from turtle import *
from draw_shapes import draw_square

# shape("turtle")

def draw_triangle():
   for i in range(3):
      forward(200)
      left(120)

def draw_polygon(num_of_sides):
   for i in range(num_of_sides):
      forward(100)
      left(60)


draw_polygon(5)

# for i in range(100):
   # draw_square()
   # draw_triangle()
   # right(5)


mainloop()