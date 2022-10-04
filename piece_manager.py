from turtle import Turtle
import game_board

class PieceManager:
    def __init__(self):
        self.active_piece = None
        self.queue = []
        self.hold_piece = []

    def swap_hold_piece(self):
        if self.hold_piece is None:
            self.hold_piece = self.active_piece
            self.active_piece = self.queue[0]

            self.queue.remove(self.active_piece)

            self.queue_new()
        else:
            temp = self.active_piece
            self.active_piece = self.hold_piece
            self.hold_piece = temp

    def queue_new(self):
        # pick random new piece
        # add to end of queue
        pass

    def next_piece(self):
        self.active_piece = self.queue[0]
        self.queue_new()

class Piece:
    def __init__(self):
        self.squares = []

    def move_left(self, left_wall):
        for square in self.squares:
            pass
            # if cant move left:
            #     return
        for square in self.squares:
            x = square.xcor()
            y = square.ycor()
            square.goto(x - 20, y)

    def move_right(self):
        for square in self.squares:
            pass
        # if cant move right:
        #     return
        for square in self.squares:
            x = square.xcor()
            y = square.ycor()
            square.goto(x + 20, y)

    def move_down(self):
        for square in self.squares:
            pass
        # if cant move down:
        #     return False
        for square in self.squares:
            x = square.xcor()
            y = square.ycor()
            square.goto(x + 20, y)
        return True
