from turtle import Turtle


class GameBoard:
    def __init__(self, square_size):
        self.square_size = square_size

        self.LEFT_WALL = -5 * self.square_size
        self.RIGHT_WALL = 5 * self.square_size
        self.TOP_WALL = 10 * self.square_size
        self.BOTTOM_WALL = -10 * self.square_size

        self.wall_turtle = Turtle()
        self.wall_turtle.hideturtle()
        self.wall_turtle.color("black")
        self.wall_turtle.pensize(5)

        self.draw_outer_wall()

        self.draw_columns()

        self.draw_rows()

    def draw_rows(self):
        self.wall_turtle.penup()
        self.wall_turtle.goto(LEFT_WALL, TOP_WALL)
        self.wall_turtle.pendown()

        for index in range(0, 10):
            self.wall_turtle.setheading(270)
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(0)
            self.wall_turtle.forward(10 * self.square_size)
            self.wall_turtle.setheading(270)
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(180)
            self.wall_turtle.forward(10 * self.square_size)

    def draw_columns(self):
        self.wall_turtle.penup()
        self.wall_turtle.goto(LEFT_WALL, TOP_WALL)
        self.wall_turtle.pendown()

        for index in range(0, 5):
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(270)
            self.wall_turtle.forward(20 * self.square_size)
            self.wall_turtle.setheading(0)
            self.wall_turtle.forward(self.square_size)
            self.wall_turtle.setheading(90)
            self.wall_turtle.forward(20 * self.square_size)
            self.wall_turtle.setheading(0)

    def draw_outer_wall(self):
        self.wall_turtle.penup()
        self.wall_turtle.goto(LEFT_WALL, TOP_WALL)
        self.wall_turtle.pendown()

        self.wall_turtle.forward(10 * self.square_size)
        self.wall_turtle.setheading(270)
        self.wall_turtle.forward(20 * self.square_size)
        self.wall_turtle.setheading(180)
        self.wall_turtle.forward(10 * self.square_size)
        self.wall_turtle.setheading(90)
        self.wall_turtle.forward(20 * self.square_size)
        self.wall_turtle.setheading(0)
