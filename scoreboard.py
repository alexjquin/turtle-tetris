from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lines = 0
        self.level = 1

        self.color("black")
        self.hideturtle()

        self.print_board()

    def print_board(self):
        self.clear()

        self.print_hold()

        self.print_next()

        self.print_lines()

        self.print_level()

    def print_next(self):
        self.penup()
        self.goto(215, 300)
        self.pendown()
        self.write("Next", align="center", font=("Arial", 20, "bold underline"))

    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.pendown()
        self.write("Game Over", align="center", font=("Arial", 40, "bold underline"))

    def print_lines(self):
        self.penup()
        self.goto(215, -100)
        self.pendown()
        self.write("Lines", align="center", font=("Arial", 20, "bold underline"))

        self.penup()
        self.goto(215, -130)
        self.pendown()
        self.write(str(self.lines), align="center", font=("Arial", 20, "normal"))

    def print_level(self):
        self.penup()
        self.goto(215, -200)
        self.pendown()
        self.write("Level", align="center", font=("Arial", 20, "bold underline"))

        self.penup()
        self.goto(215, -230)
        self.pendown()
        self.write(str(self.level), align="center", font=("Arial", 20, "normal"))

    def print_hold(self):
        self.penup()
        self.goto(-215, 300)
        self.pendown()
        self.write("Hold", align="center", font=("Arial", 20, "bold underline"))
        pass

    def add(self, num_lines):
        self.lines += num_lines
        self.print_lines()

        self.print_board()

    def level_up(self):
        self.level += 1
        self.print_level()

        self.print_board()
