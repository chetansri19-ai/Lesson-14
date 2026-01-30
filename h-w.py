#Writing a program to make a square using turtle module
import turtle    #importing library
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300,400)
square=turtle.Turtle() #defined variable
side_length=100 #variable
#iterate loop for total number of sides
for i in range(4):
    square.forward(side_length)
    square.right(90)
turtle.done()