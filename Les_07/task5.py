"""
Task 5:
Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
If the board is valid return 'Finished!', otherwise return 'Try again!'
"""

# Нет совпадений по вертикали и горизонтали

table = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [2, 3, 4, 5, 6, 7, 8, 9, 1],
         [3, 4, 5, 6, 7, 8, 9, 1, 2],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [5, 6, 7, 8, 9, 1, 2, 3, 4],
         [6, 7, 8, 9, 1, 2, 3, 4, 5],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [8, 9, 1, 2, 3, 4, 5, 6, 7],
         [9, 1, 2, 3, 4, 5, 6, 7, 8]]



# Finished!
'''
table = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
         [4, 9, 8, 2, 6, 1, 3, 7, 5],
         [7, 5, 6, 3, 8, 4, 2, 1, 9],
         [6, 4, 3, 1, 5, 8, 7, 9, 2],
         [5, 2, 1, 7, 9, 3, 8, 4, 6],
         [9, 8, 7, 4, 2, 6, 5, 3, 1],
         [2, 1, 4, 9, 3, 5, 6, 8, 7],
         [3, 6, 5, 8, 1, 7, 9, 2, 4],
         [8, 7, 9, 6, 4, 2, 1, 5, 3]]
'''

# Try again!
'''
table = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
         [4, 9, 8, 2, 6, 1, 3, 7, 5],
         [7, 5, 6, 3, 8, 4, 2, 1, 9],
         [6, 4, 3, 1, 5, 8, 7, 9, 2],
         [5, 2, 1, 7, 9, 3, 8, 4, 6],
         [9, 8, 7, 4, 2, 6, 5, 3, 1],
         [2, 1, 4, 9, 3, 5, 6, 8, 7],
         [3, 6, 5, 8, 1, 7, 9, 2, 4],
         [8, 7, 9, 6, 4, 2, 1, 3, 5]]
'''

def done_or_not(table):
    """If the board is valid return 'Finished!', otherwise return 'Try again!'"""
    list_sets = []

    # Вертикаль
    counter = 0
    while counter < 9:
        ver = [i[counter] for i in table]
        list_sets.append(len(set(ver)))
        counter += 1

    # Горизонталь
    hor = [len(set(i)) for i in table]
    list_sets.extend(hor)

    # Массив 3х3
    len_sets = []
    list_num = []
    row = 0
    col = 0
    while row < 9:
        while col < 9:
            list_num.append(table[row][col])
            col += 1
            if col == 3:
                col = 0
                break
            elif col == 6:
                col = 3
                break
            elif col == 9:
                col = 6
                break
        if len(list_num) == 9:
            len_sets.append(len(set(list_num)))
            list_num.clear()
        if len(len_sets) == 3:
            col = 3
        elif len(len_sets) == 6:
            col = 6
        if row == 8 and len(len_sets) != 9:
            row = -1
        row += 1
    list_sets.extend(len_sets)

    if len(set(list_sets)) > 1:
        result = 'Try again!'
    else:
        result = 'Finished!'

    return result


print(done_or_not(table))


