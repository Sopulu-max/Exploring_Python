import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
alex = turtle.Turtle()
tess = turtle.Turtle()

# tess.shape("turtle")
tess.color("blue")
# tess.penup() # this is new
size = 20

def draw_square(length):
    for i in range(4):
        alex.forward(length)
        alex.left(90)

draw_square(100)


for i in range(30):
    tess.stamp() # leave an impression on the canvas
    size = size + 3 # increase the size on every iteration
    tess.forward(size) # move tess along
    tess.right(24) # and turn her
wn.mainloop()