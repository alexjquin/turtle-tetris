import random
from tetronimo import Tetronimo

WIDTH = 10
HEIGHT = 20

QUEUE_ORIGINS = [(215, 285), (215, 195), (215, 105)]
ORIGIN_COORDINATES = (15, 285)
ORIGIN_INDEX = (5, 19)

HOLD_COORDINATES = (-215, 285)


class PieceManager:
    def __init__(self, square_size):
        self.square_size = square_size

        # 10 x 20 array of None to begin
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

        self.active_piece.draw_piece(ORIGIN_COORDINATES, ORIGIN_INDEX)

    # initialize 20x10 array of None
    def initialize_board(self):
        self.board = []
        for row_index in range(0, 20):
            row = []
            for col_index in range(0, 10):
                row.append(None)
            self.board.append(row)

    def swap_hold_piece(self, event=None):
        if self.hold_piece is None:
            self.hold_piece = self.active_piece
            self.hold_piece.draw_piece(HOLD_COORDINATES)

            self.next_piece()
        else:
            temp = self.active_piece
            self.active_piece = self.hold_piece
            self.hold_piece = temp

            self.hold_piece.draw_piece(HOLD_COORDINATES)
            self.active_piece.draw_piece(ORIGIN_COORDINATES, ORIGIN_INDEX)

    def queue_new(self):
        # pick random new piece
        # add to end of queue
        new_piece = Tetronimo()
        self.queue.append(new_piece)

        self.draw_queue()

    def draw_queue(self):
        for index, piece in enumerate(self.queue):
            piece.draw_piece(QUEUE_ORIGINS[index])

    def next_piece(self):
        self.active_piece = self.queue[0]
        self.queue.remove(self.active_piece)
        self.queue_new()

        self.active_piece.draw_piece(ORIGIN_COORDINATES, ORIGIN_INDEX)

    #
    def move_left(self, event):
        # Check if piece can move left
        for turt in self.active_piece.turtles:
            if turt.x_index == 0 or self.board[turt.y_index][turt.x_index - 1] is not None:
                return
            # elif square is occupied by piece already on board

        # Move piece left
        for turt in self.active_piece.turtles:
            turt.goto(turt.xcor() - self.square_size, turt.ycor())
            turt.x_index -= 1

    def move_right(self, event):
        # Check if piece can move right
        for turt in self.active_piece.turtles:
            if turt.x_index == 9 or self.board[turt.y_index][turt.x_index + 1] is not None:
                return
            # elif square is occupied by piece already on board

        # Move piece right
        for turt in self.active_piece.turtles:
            turt.goto(turt.xcor() + self.square_size, turt.ycor())
            turt.x_index += 1

    def move_down(self, event=None):
        for turt in self.active_piece.turtles:
            if turt.y_index == 0 or self.board[turt.y_index - 1][turt.x_index] is not None:
                return False
            # elif square is occupied by piece already on board
        for turt in self.active_piece.turtles:
            turt.goto(turt.xcor(), turt.ycor() - self.square_size)
            turt.y_index -= 1
        return True

    def check_lines(self):
        return 0

    def is_full(self):
        for space in self.board[19]:
            if space is not None:
                return True

        return False

    # rotate around square[1]
    def finish_active(self):
        for turt in self.active_piece.turtles:
            self.board[turt.y_index][turt.x_index] = turt
