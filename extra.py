#Writing a program to make a 12 sided star polygon with two triangle overlapping each other while one is facing up and one is facing down using turtle module, without for loop.
import turtle #importing library

turtle.Screen().bgcolor("Aqua")
board=turtle.Turtle()

#first triangle for star
board.forward(100)  #draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()