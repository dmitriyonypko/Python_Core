"""Task 3:
Tic-Tac-Toe Checker
If we were to set up a Tic-Tac-Toe game,
we would want to know whether the board's current state is solved,
wouldn't we? Our goal is to create a function that will check that for us!
Assume that the board comes in the form of a 3x3 array,
where the value is 0 if a spot is empty,
1 if it is an "X",or 2 if it is an "O", like so:
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]

We want our function to return:
-1 if the board is not yet finished (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""


import numpy


board = [[2, 1, 1],
         [1, 2, 2],
         [1, 2, 1]]


def game_tic_tac_toe(board):
    """"Tic-Tac-Toe Checker"""
    list_sides = []
    len_side = len(board[0])
    # Вертикаль
    counter = 0
    while counter < len_side:
        ver = [i[counter] for i in board]
        list_sides.append(numpy.prod(ver))
        counter += 1
    # Горизонталь
    list_sides.extend([numpy.prod(i) for i in board])
    # Диагональ 1
    diag = [board[i][i] for i in range(len_side)]
    list_sides.append(numpy.prod(diag))
    # Диагональ 2
    diag = [board[len_side - 1 - i][i] for i in range(len_side)]
    list_sides.append(numpy.prod(diag))

    if 2 ** len_side in list_sides:
        result = 2
    elif 1 in list_sides:
        result = 1
    elif 0 not in list_sides:
        result = 0
    else:
        result = -1
    return result

print(game_tic_tac_toe(board))
