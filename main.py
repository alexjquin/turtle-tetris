import time
import turtle
from turtle import Screen

import game_board
from piece_manager import PieceManager

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

speed = 1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Tetris")
screen.bgpic("resources/beach.gif")
screen.tracer(0)
screen.listen()

# TODO: Draw board
board.draw_board()

# TODO: Build piece manager
piece_manager = PieceManager()

# TODO: Build Scoreboard

canvas = turtle.getcanvas()
canvas.bind("<Left>", piece_manager.move_left)
canvas.bind("<Down>", piece_manager.move_down)
canvas.bind("<Right>", piece_manager.move_right)
canvas.bind("<Control_L>", piece_manager.swap_hold_piece)

screen.update()

game_is_on = True

while game_is_on:
    if not piece_manager.move_down():
        piece_manager.next_piece()

    screen.update()

# 10*20 squares

screen.mainloop()