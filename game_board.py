from turtle import Turtle


HEIGHT = 20
WIDTH = 10

class GameBoard:
    def __init__(self, square_size):
        self.square_size = square_size

        self.wall_turtle = Turtle()
        self.wall_turtle.hideturtle()
        self.wall_turtle.color("#29929e")
        self.wall_turtle.pensize(3)

        self.draw_outer_wall()

        self.draw_columns()

        self.draw_rows()

    def draw_rows(self):
        self.wall_turtle.penup()
        self.wall_turtle.goto(-WIDTH / 2 * self.square_size, HEIGHT / 2 * self.square_size)
        self.wall_turtle.pendown()

        for index in range(0, 10):
            self.wall_turtle.setheading(270)
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(0)
            self.wall_turtle.forward(WIDTH * self.square_size)
            self.wall_turtle.setheading(270)
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(180)
            self.wall_turtle.forward(WIDTH * self.square_size)

    def draw_columns(self):
        self.wall_turtle.penup()
        self.wall_turtle.goto(-WIDTH / 2 * self.square_size, HEIGHT / 2 * self.square_size)
        self.wall_turtle.pendown()

        for index in range(0, 5):
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(270)
            self.wall_turtle.forward(HEIGHT * self.square_size)
            self.wall_turtle.setheading(0)
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(90)
            self.wall_turtle.forward(HEIGHT * self.square_size)
            self.wall_turtle.setheading(0)

    def draw_outer_wall(self):
        self.wall_turtle.penup()
        self.wall_turtle.goto(-WIDTH / 2 * self.square_size, HEIGHT / 2 * self.square_size)
        self.wall_turtle.pendown()

        self.wall_turtle.forward(WIDTH * self.square_size)
        self.wall_turtle.setheading(270)
        self.wall_turtle.forward(HEIGHT * self.square_size)
        self.wall_turtle.setheading(180)
        self.wall_turtle.forward(WIDTH * self.square_size)
        self.wall_turtle.setheading(90)
        self.wall_turtle.forward(HEIGHT * self.square_size)
        self.wall_turtle.setheading(0)
