#Writing a program to make a 12-sided star polygon using turtle module and angles. It has to be drwan with two triagles with in it one facing up and other facing down while overlapping each other
import turtle  #importing library
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(1000,1000)
star_polygon=turtle.Turtle() #defined variable
num_side=12 #variable
side_length=150
angle=150 #angle for star polygon
#iterate loop for total number of sides
for i in range(num_side):
    star_polygon.forward(side_length)
    star_polygon.right(angle)

turtle.done()