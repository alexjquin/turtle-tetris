import threading
import time
import turtle
from turtle import Screen

import tkinter as tk

from game_board import GameBoard
from piece_manager import PieceManager

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SQUARE_SIZE = 30

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Tetris")
screen.bgpic("resources/beach.gif")
screen.tracer(0)
screen.listen()

game_board = GameBoard(SQUARE_SIZE)

# TODO: Build piece manager
piece_manager = PieceManager()

# TODO: Build Scoreboard
# scoreboard = Scoreboard()

canvas = turtle.getcanvas()
# canvas.bind("<Left>", piece_manager.move_left)
canvas.bind("<Down>", piece_manager.move_down)
# canvas.bind("<Right>", piece_manager.move_right)
# canvas.bind("<Control_L>", piece_manager.swap_hold_piece)

screen.update()

game_is_on = True
delay = 1

def move_down_event():
    if not piece_manager.move_down():
        # num_lines = piece_manager.check_lines()
        # scoreboard.add(num_lines)
        piece_manager.get_next_piece()
    turtle.ontimer(move_down_event, t=delay * 1000)

turtle.ontimer(move_down_event, t=delay * 1000)

while game_is_on:
    # if not piece_manager.move_down():
    #     pass
#         # num_lines = game_board.check_lines()
#         # scoreboard.add(num_lines)
#         # piece_manager.get_next_piece()
#
#
#
    screen.update()


screen.mainloop()