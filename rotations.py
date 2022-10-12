def out_of_bounds(x, y):
    print(f"{y}, {x}")
    return x < 0 or x > 9 or y < 0 or y > 19


def is_valid_rotation(x, y, board):
    print(f"Board[y][x] = {board[y][x]}" )
    print(f"Out of Bounds: {out_of_bounds(x, y)}")
    return not out_of_bounds(x, y) and board[y][x] is None


def rotate_i_left(active_piece, board, square_size):
    turt_0 = active_piece.turtles[0]
    # turtles[1] is rotation center and doesn't move
    turt_2 = active_piece.turtles[2]
    turt_3 = active_piece.turtles[3]

    if active_piece.rotation == 1:
        i_rotation_1_to_4(turt_0, turt_2, turt_3, board, square_size)

    elif active_piece.rotation == 2:
        i_rotation_4_to_3(turt_0, turt_2, turt_3, board, square_size)

    elif active_piece.rotation == 3:
        i_rotation_3_to_2(turt_0, turt_2, turt_3, board, square_size)

    elif active_piece.rotation == 4:
        i_rotation_2_to_1(turt_0, turt_2, turt_3, board, square_size)

    active_piece.rotate_right()


def rotate_i_right(active_piece, board, square_size):
    turt_0 = active_piece.turtles[0]
    # turtles[1] is rotation center and doesnt move
    turt_2 = active_piece.turtles[2]
    turt_3 = active_piece.turtles[3]

    if active_piece.rotation == 1:
        i_rotation_1_to_2(turt_0, turt_2, turt_3, board, square_size)

    elif active_piece.rotation == 2:
        i_rotation_2_to_3(turt_0, turt_2, turt_3, board, square_size)

    elif active_piece.rotation == 3:
        i_rotation_3_to_4(turt_0, turt_2, turt_3, board, square_size)

    elif active_piece.rotation == 4:
        i_rotation_4_to_1(turt_0, turt_2, turt_3, board, square_size)

    active_piece.rotate_right()


def i_rotation_1_to_2(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x + 1
    turt_0_new_y = turt_0_y + 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        print(f"invalid 1-2 rotation for turtle 0")
        return

    turt_2_new_x = turt_2_x - 1
    turt_2_new_y = turt_2_y - 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        print(f"invalid 1-2 rotation for turtle 2")
        return

    turt_3_new_x = turt_3_x - 2
    turt_3_new_y = turt_3_y - 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        print(f"invalid 1-2 rotation for turtle 3")
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() + square_size, turt_0.ycor() + square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() - square_size, turt_2.ycor() - square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() - 2 * square_size, turt_3.ycor() - 2 * square_size)


def i_rotation_2_to_3(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x + 1
    turt_0_new_y = turt_0_y - 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        return

    turt_2_new_x = turt_2_x - 1
    turt_2_new_y = turt_2_y + 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        return

    turt_3_new_x = turt_3_x - 2
    turt_3_new_y = turt_3_y + 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() + square_size, turt_0.ycor() - square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() - square_size, turt_2.ycor() + square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() - 2 * square_size, turt_3.ycor() + 2 * square_size)


def i_rotation_3_to_4(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x - 1
    turt_0_new_y = turt_0_y - 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        return

    turt_2_new_x = turt_2_x + 1
    turt_2_new_y = turt_2_y + 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        return

    turt_3_new_x = turt_3_x + 2
    turt_3_new_y = turt_3_y + 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() - square_size, turt_0.ycor() - square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() + square_size, turt_2.ycor() + square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() + 2 * square_size, turt_3.ycor() + 2 * square_size)


def i_rotation_4_to_1(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x - 1
    turt_0_new_y = turt_0_y + 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        return

    turt_2_new_x = turt_2_x + 1
    turt_2_new_y = turt_2_y - 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        return

    turt_3_new_x = turt_3_x + 2
    turt_3_new_y = turt_3_y - 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() - square_size, turt_0.ycor() + square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() + square_size, turt_2.ycor() - square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() + 2 * square_size, turt_3.ycor() - 2 * square_size)


def i_rotation_1_to_4(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x + 1
    turt_0_new_y = turt_0_y - 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        return

    turt_2_new_x = turt_2_x - 1
    turt_2_new_y = turt_2_y + 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        return

    turt_3_new_x = turt_3_x - 2
    turt_3_new_y = turt_3_y + 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() + square_size, turt_0.ycor() - square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() - square_size, turt_2.ycor() + square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() - 2 * square_size, turt_3.ycor() + 2 * square_size)


def i_rotation_4_to_3(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x + 1
    turt_0_new_y = turt_0_y + 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        return

    turt_2_new_x = turt_2_x - 1
    turt_2_new_y = turt_2_y - 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        return

    turt_3_new_x = turt_3_x - 2
    turt_3_new_y = turt_3_y - 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() + square_size, turt_0.ycor() + square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() - square_size, turt_2.ycor() - square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() - 2 * square_size, turt_3.ycor() - 2 * square_size)


def i_rotation_3_to_2(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x - 1
    turt_0_new_y = turt_0_y + 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        return

    turt_2_new_x = turt_2_x + 1
    turt_2_new_y = turt_2_y - 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        return

    turt_3_new_x = turt_3_x + 2
    turt_3_new_y = turt_3_y - 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() - square_size, turt_0.ycor() + square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() + square_size, turt_2.ycor() - square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() + 2 * square_size, turt_3.ycor() - 2 * square_size)


def i_rotation_2_to_1(turt_0, turt_2, turt_3, board, square_size):
    turt_0_x = turt_0.x_index
    turt_0_y = turt_0.y_index

    # turtles[1] is rotation center and doesnt move

    turt_2_x = turt_2.x_index
    turt_2_y = turt_2.y_index

    turt_3_x = turt_3.x_index
    turt_3_y = turt_3.y_index

    turt_0_new_x = turt_0_x - 1
    turt_0_new_y = turt_0_y - 1
    if not is_valid_rotation(turt_0_new_x, turt_0_new_y, board):
        return

    turt_2_new_x = turt_2_x + 1
    turt_2_new_y = turt_2_y + 1
    if not is_valid_rotation(turt_2_new_x, turt_2_new_y, board):
        return

    turt_3_new_x = turt_3_x + 2
    turt_3_new_y = turt_3_y + 2
    if not is_valid_rotation(turt_3_new_x, turt_3_new_y, board):
        return

    turt_0.x_index = turt_0_new_x
    turt_0.y_index = turt_0_new_y
    turt_0.goto(turt_0.xcor() - square_size, turt_0.ycor() - square_size)

    turt_2.x_index = turt_2_new_x
    turt_2.y_index = turt_2_new_y
    turt_2.goto(turt_2.xcor() + square_size, turt_2.ycor() + square_size)

    turt_3.x_index = turt_3_new_x
    turt_3.y_index = turt_3_new_y
    turt_3.goto(turt_3.xcor() + 2 * square_size, turt_3.ycor() + 2 * square_size)
