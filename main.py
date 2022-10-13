import turtle
from turtle import Screen

from game_board import GameBoard
from piece_manager import PieceManager
from scoreboard import Scoreboard


def march_turtles_off(full_rows):
    for step in range(0, 10):  # 10 steps to move off board
        for row in full_rows:
            for turt in row:
                turt.forward(SQUARE_SIZE)
                turt.x_index -= 1

                if turt.x_index < 0:
                    turt.hideturtle()
            screen.update()


def move_down_on_timer():
    global delay
    global game_is_on
    global swapped

    if not piece_manager.move_down():
        piece_manager.finish_active()
        swapped = False

        if piece_manager.is_full():
            game_is_on = False
            return
        else:
            num_lines, full_rows = piece_manager.check_lines()

            if num_lines > 0:
                scoreboard.add(num_lines)

                march_turtles_off(full_rows)

                piece_manager.shift_pieces_down(full_rows)

                if scoreboard.lines > 0 and scoreboard.lines % 10 == 0:
                    scoreboard.level_up()
                    delay *= 0.9

        piece_manager.next_piece()

    global timer_id
    timer_id = canvas.after(int(delay * 1000), move_down_on_timer)


def swap_piece_event(event=None):
    global swapped

    if not swapped:
        piece_manager.swap_hold_piece()
        swapped = True


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
canvas.bind("<Down>", piece_manager.move_down)
canvas.bind("<Right>", piece_manager.move_right)
canvas.bind("<Control_L>", swap_piece_event)
canvas.bind("<Up>", piece_manager.rotate_right)
canvas.bind("<z>", piece_manager.rotate_left)

screen.update()

game_is_on = True

delay = 1

swapped = False

timer_id = canvas.after(int(delay * 1000), move_down_on_timer)

while game_is_on:
    screen.update()

scoreboard.game_over()
screen.mainloop()
