import random
from turtle import Turtle
import game_board

WIDTH = 10
HEIGHT = 20

PIECES = ["O", "I", "S", "Z", "L", "J", "T"]
O = [(-1, 0), (-1, -1), (0, 0), (0, -1)]
I = [(-1, 0), (0, 0), (1, 0), (2, 0)]
S = [(0, 0), (1, 0), (-1, -1), (0, -1)]
Z = [(-1, 0), (0, 0), (0, -1), (1, -1)]
L = [(-1, -1), (0, -1), (1, -1), (1, 0)]
J = [(-1, 0), (-1, -1), (0, -1), (1, -1)]
T = [(-1, -1), (0, 0), (0, -1), (1, -1)]

O_COLOR = "#edf200"
I_COLOR = "#00d8f2"
S_COLOR = "#ea0000"
Z_COLOR = "#64ad23"
L_COLOR = "#f28600"
J_COLOR = "#f24db2"
T_COLOR = "#97008e"

ORIGIN = (15, 285)

QUEUE_ORIGINS = [(215, 285), (215, 195), (215, 105)]


class PieceManager:
    def __init__(self, square_size):
        self.square_size = square_size

        self.board = None
        self.initialize_board()

        self.active_piece = None
        self.queue = []
        self.hold_piece = None

        self.left_wall = -WIDTH / 2 * self.square_size
        self.right_wall = WIDTH / 2 * self.square_size
        self.top_wall = HEIGHT / 2 * self.square_size
        self.bottom_wall = -HEIGHT / 2 * self.square_size

        for index in range(0, 3):
            self.queue_new()

        self.next_piece()

        self.draw_queue()

        self.active_piece.draw_piece(ORIGIN)

    # initialize 20x10 array of None
    def initialize_board(self):
        self.board = []
        for row_index in range(0, 20):
            row = []
            for col_index in range(0, 10):
                row.append(None)
            self.board.append(row)

    # def swap_hold_piece(self):
    #     if self.hold_piece is None:
    #         self.hold_piece = self.active_piece
    #         self.active_piece = self.queue[0]
    #
    #         self.queue.remove(self.active_piece)
    #
    #         self.queue_new()
    #     else:
    #         temp = self.active_piece
    #         self.active_piece = self.hold_piece
    #         self.hold_piece = temp
    #
    def queue_new(self):
        # pick random new piece
        # add to end of queue
        new_shape = random.choice(PIECES)
        new_piece = Piece(new_shape)
        self.queue.append(new_piece)

    def draw_queue(self):
        for index, piece in enumerate(self.queue):
            piece.draw_piece(QUEUE_ORIGINS[index])

    def next_piece(self):
        self.active_piece = self.queue[0]
        self.queue.remove(self.active_piece)
        self.queue_new()

    #
    def move_left(self, event):
        # Check if piece can move left
        for turt in self.active_piece.turtles:
            x = turt.xcor()
            if x - self.square_size < self.left_wall:
                return
            # elif square is occupied by piece already on board

        # Move piece left
        for turt in self.active_piece.turtles:
            x = turt.xcor()
            y = turt.ycor()
            turt.goto(x - self.square_size, y)

    def move_right(self, event):
        # Check if piece can move right
        for turt in self.active_piece.turtles:
            x = turt.xcor()
            if x + self.square_size > self.right_wall:
                return
            # elif square is occupied by piece already on board

        # Move piece right
        for turt in self.active_piece.turtles:
            x = turt.xcor()
            y = turt.ycor()
            turt.goto(x + self.square_size, y)

    def move_down(self):
        for turt in self.active_piece.turtles:
            y = turt.ycor()
            if y - self.square_size < self.bottom_wall:
                return False
            # elif square is occupied by piece already on board
        for turt in self.active_piece.turtles:
            x = turt.xcor()
            y = turt.ycor()
            turt.goto(x, y - self.square_size)
        return True

    def check_lines(self):
        return 0

    def is_full(self):
        return False


def new_turtle(color):
    tim = Turtle()
    tim.shape("turtle")
    tim.color("black", color)
    tim.penup()
    tim.setheading(270)
    tim.shapesize(1.4)

    return tim


class Piece:
    def __init__(self, new_shape):
        self.turtles = []

        if new_shape == "O":
            self.make_piece(O_COLOR)
            self.shape = O
        elif new_shape == "I":
            self.make_piece(I_COLOR)
            self.shape = I
        elif new_shape == "S":
            self.make_piece(S_COLOR)
            self.shape = S
        elif new_shape == "Z":
            self.make_piece(Z_COLOR)
            self.shape = Z
        elif new_shape == "L":
            self.make_piece(L_COLOR)
            self.shape = L
        elif new_shape == "J":
            self.make_piece(J_COLOR)
            self.shape = J
        elif new_shape == "T":
            self.make_piece(T_COLOR)
            self.shape = T

    def make_piece(self, color: str):
        for index in range(0, 4):
            tim = new_turtle(color)
            self.turtles.append(tim)

    def draw_piece(self, origin):
        for index, coordinates in enumerate(self.shape):
            self.turtles[index].goto(coordinates[0] * 30 + origin[0], coordinates[1] * 30 + origin[1])

    # rotate around square[1]
