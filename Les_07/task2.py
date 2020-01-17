"""Task 2:
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]
"""


some_list = [False, 1, 0, 1, 2, 0, 1, 3, 0, "a"]


def moveZeros(some_list):
    """Moves all of the zeros to the end."""
    lis = []
    for index, item in enumerate(some_list):
        if type(item) is int:
            if item == 0:
                lis.append(some_list.pop(index))
    some_list.extend(lis)
    return some_list


print(some_list)
print(moveZeros(some_list))


