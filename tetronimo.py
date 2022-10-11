import random
from turtle import Turtle


PIECES = ["O", "I", "S", "Z", "L", "J", "T"]

O_COLOR = "#edf200"
I_COLOR = "#00d8f2"
S_COLOR = "#ea0000"
Z_COLOR = "#64ad23"
L_COLOR = "#f28600"
J_COLOR = "#f24db2"
T_COLOR = "#97008e"

O = [(-1, 0), (-1, -1), (0, 0), (0, -1)]
I = [(-1, 0), (0, 0), (1, 0), (2, 0)]
S = [(0, 0), (1, 0), (-1, -1), (0, -1)]
Z = [(-1, 0), (0, 0), (0, -1), (1, -1)]
L = [(-1, -1), (0, -1), (1, -1), (1, 0)]
J = [(-1, 0), (-1, -1), (0, -1), (1, -1)]
T = [(-1, -1), (0, 0), (0, -1), (1, -1)]


def new_turtle(color):
    tim = Turtle()
    tim.shape("turtle")
    tim.color("black", color)
    tim.penup()
    tim.setheading(270)
    tim.shapesize(1.5)

    return tim


class Tetronimo:
    def __init__(self):
        new_shape = random.choice(PIECES)

        self.x_index = -1
        self.y_index = -1

        self.turtles = []

        if new_shape == "O":
            self.make_shape(O_COLOR)
            self.shape = O
        elif new_shape == "I":
            self.make_shape(I_COLOR)
            self.shape = I
        elif new_shape == "S":
            self.make_shape(S_COLOR)
            self.shape = S
        elif new_shape == "Z":
            self.make_shape(Z_COLOR)
            self.shape = Z
        elif new_shape == "L":
            self.make_shape(L_COLOR)
            self.shape = L
        elif new_shape == "J":
            self.make_shape(J_COLOR)
            self.shape = J
        elif new_shape == "T":
            self.make_shape(T_COLOR)
            self.shape = T

    def make_shape(self, color: str):
        for index in range(0, 4):
            tim = new_turtle(color)
            self.turtles.append(tim)

    def draw_piece(self, initial_coordinates, initial_index=None):
        for index, coordinates in enumerate(self.shape):
            self.turtles[index].goto(coordinates[0] * 30 + initial_coordinates[0],
                                     coordinates[1] * 30 + initial_coordinates[1])

            if initial_index is not None:
                self.x_index = coordinates[0] + initial_index[0]
                self.y_index = coordinates[1] + initial_index[1]