import threading
import time
import turtle
from turtle import Screen

import tkinter as tk

from game_board import GameBoard
from piece_manager import PieceManager
from scoreboard import Scoreboard


def move_down_event(event=None):
    global delay
    global game_is_on

    if not piece_manager.move_down():
        if piece_manager.is_full():
            game_is_on = False
        else:
            num_lines = piece_manager.check_lines()
            scoreboard.add(num_lines)
            piece_manager.next_piece()

            if scoreboard.lines > 0 and scoreboard.lines % 10:
                scoreboard.level_up()
                delay *= 0.9
    turtle.ontimer(move_down_event, t=delay * 1000)


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 800
SQUARE_SIZE = 30

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Tetris")
screen.bgpic("resources/beach.gif")
screen.tracer(0)
screen.listen()

game_board = GameBoard(SQUARE_SIZE)

piece_manager = PieceManager(SQUARE_SIZE)

scoreboard = Scoreboard()

canvas = turtle.getcanvas()
canvas.bind("<Left>", piece_manager.move_left)
canvas.bind("<Down>", move_down_event)
canvas.bind("<Right>", piece_manager.move_right)
# canvas.bind("<Control_L>", piece_manager.swap_hold_piece)

screen.update()

global game_is_on
game_is_on = True

global delay
delay = 1

turtle.ontimer(move_down_event, t=delay * 1000)

while game_is_on:
    screen.update()

# scoreboard.game_over()
screen.mainloop()
