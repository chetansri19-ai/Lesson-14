#Writing a program to make a polygon using turtle module
import turtle    #importing library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(1000,1000)
polygon=turtle.Turtle() #defined variable

num_side=6 #variable
side_length=70
angle=360.0/num_side
#iterate loop for total number of sides
for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()