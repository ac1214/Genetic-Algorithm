from turtle import Turtle, Screen



screen = Screen()
screen.setup(width=600, height=700)

turtle = Turtle()

# Draw the x-axis
turtle.pencolor("black")
turtle.penup()
turtle.goto(-250, -300)
turtle.pendown()
turtle.goto(250, -300)

numbers = 0
turtle.penup()
# Draw x Axis
for i in range(-250, 300, 50):
    print(i)
    turtle.goto(i, -305)
    turtle.write(str(numbers))
    numbers += 50

x_points = [i for i in range(0, 500)]
turtle.penup()
turtle.goto(-250, -300)
turtle.pendown()
for ind, y_value in enumerate(x_points):
    print(ind)
    turtle.goto(-250 + ind, -300 + y_value)


screen.mainloop()