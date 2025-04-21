#TurtleGraphics.py
#Name: Megann Wegner    
#Date: 4/20/2025
#Assignment: Lab 4

import turtle 

def drawPolygon(bob, sides, size):
    direction = 360 / sides
    for i in range(sides):
        bob.forward(size)
        bob.left(direction)

def fillQuadrant(bob, quadrant, size):
    half = size / 2
    bob.fillcolor("green")

    bob.penup()
    if quadrant == 1:
        bob.goto(-200, 0)
    elif quadrant == 2:
        bob.goto(0, 0)
    elif quadrant == 3:
        bob.goto(-200, -200)
    elif quadrant == 4:
        bob.goto(0, -200)
    else:
        print("Not a quadrant. ")
        return

    bob.pendown()
    bob.begin_fill()
    for i in range(4):
        bob.forward(half)
        bob.left(90)
    bob.end_fill()
    
def drawSquaresInSquares(bob, total, start):
    current_size = start
    smaller = start/total
    for n in range(total):
        bob.penup()
        bob.goto(-current_size / 2, -current_size / 2) 
        bob.pendown()
        drawPolygon(bob, 4, current_size)
        current_size -= smaller

def main():
    bob = turtle.Turtle()
    bob.penup()
    bob.goto(-200, -200)
    bob.pendown()
    size = 400
    drawPolygon(bob, 4, size)
    quadrant = int(input("Pick quadrant 1, 2, 3, or 4. "))
    fillQuadrant(bob, quadrant, size)
   
    start = 400
    total = int(input("How many nested squares do you want? "))
    drawSquaresInSquares(bob, total, start)
    turtle.done()
    
main()
