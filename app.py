import turtle
import random

f = turtle
f.setup(width=1000, height=1000, startx=250, starty=0)

while True:

    coin = random.randint(1, 2)  # numbers for coin flip
    angle = random.randint(5, 179)  # random angle to move at later
    move_distance = random.randint(25, 100)  # random distance to move at later

    if coin == 1:  # this is just a simple if else coinflip that stores the result in a variable "result"
        print("Heads")
        result = "H"
    else:
        print("Tails")
        result = "T"

    if result == "T":  # this is to determine if the turtle should turn left or right
        f.left(angle)
        f.forward(move_distance)

    else:
        f.right(angle)
        f.forward(move_distance)

    if f.distance(0, 0) > 500:  # this exits the loop
        break

# one thing I didn't do was design the turtle, you can make that however you want
# you can delete all of the hashmark text
