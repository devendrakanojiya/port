import turtle

def draw_goku(x, y, size):
  # Move the turtle to starting position
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()

  # Draw the head
  turtle.fillcolor("orange")
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()

  # Draw the eyes
  turtle.penup()
  turtle.goto(x - size/3, y + size/2)
  turtle.pendown()
  turtle.fillcolor("black")
  turtle.begin_fill()
  turtle.circle(size/8)
  turtle.end_fill()

  turtle.penup()
  turtle.goto(x + size/3, y + size/2)
  turtle.pendown()
  turtle.fillcolor("black")
  turtle.begin_fill()
  turtle.circle(size/8)
  turtle.end_fill()

  # Draw the hair
  turtle.penup()
  turtle.goto(x, y + size)
  turtle.pendown()
  turtle.fillcolor("black")
  turtle.begin_fill()
  turtle.circle(size * 1.5, 180)
  turtle.left(90)
  turtle.forward(size * 2)
  turtle.right(90)
  turtle.circle(-size * 1.5, 180)
  turtle.end_fill()

  # Draw the aura
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.fillcolor("yellow")
  turtle.begin_fill()
  turtle.circle(size * 1.5)
  turtle.end_fill()

# Set the background color and screen size
turtle.bgcolor("white")
turtle.screensize(600, 600)

# Draw the character
draw_goku(0, 0, 100)

# Hide the turtle and exit on click
turtle.exitonclick()
