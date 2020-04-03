from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=700)

X_OFFSET = -250
Y_OFFSET = -300


class Graph:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()

        self.draw_axis()
        self.addInitialPoint(0)

    def draw_axis(self):
        # Draw the x-axis
        self.turtle.pencolor("black")
        self.turtle.penup()
        self.turtle.goto(-250, -300)
        self.turtle.pendown()
        self.turtle.goto(250, -300)

        numbers = 0
        self.turtle.penup()
        # Draw x Axis
        for i in range(-250, 300, 50):
            # print(i)
            self.turtle.goto(i, -315)
            self.turtle.write(str(numbers))
            numbers += 50

        self.turtle.goto(-250, -300)
        self.turtle.pendown()
        self.turtle.goto(-250, 300)

        # Dray y Axis
        self.turtle.penup()
        numbers = 0
        for i in range(-300, 300, 50):
            self.turtle.goto(-270, i)
            self.turtle.write(str(numbers))
            numbers += 50

    def addNewPoint(self, newX, newY):
        self.turtle.pendown()
        self.turtle.goto(X_OFFSET + newX, Y_OFFSET + newY)
        self.turtle.penup()

    def addInitialPoint(self, initialY):
        self.turtle.goto(X_OFFSET, Y_OFFSET)
        self.turtle.penup()
        self.turtle.goto(X_OFFSET, Y_OFFSET + initialY)
        self.turtle.pendown()

    def click_to_exit(self):
        screen.exitonclick()
