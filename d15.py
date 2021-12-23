# Gabe Banks
# 12/14/21
# Advent of Code day 15

data = """"""

data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

import numpy as np
from collections import Counter

data = data.split("\n")
data = [ [ int(y) for y in x] for x in data ]
print(data)

# Part 1
print("PART 1:")
board = np.array(data)
print(board)

path = []

def compare(x, y):

    right = 10
    down = 10

    if y < board.shape[0]-1:
        down = board[y+1, x]
    if x < board.shape[1]-1:
        right = board[y, x+1]
    
    if right+down == 20:
        return
    elif right < down:
        path.append(board[x+1, y])
        compare(x+1, y)
    elif down < right:
        path.append(board[x, y+1])
        compare(x, y+1)
    else:
        current = board[y+1,x]
        right_options = []
        dx = 1
        down_options = []
        dy = 1

        while dy+y < board.shape[0]-1 and board[dy+y, x] != current:
            if x + 1 < board.shape[1]:
                down_options.append(board[dy+y,x+1])
            if x - 1 >= 0:
                down_options.append(board[dy+y,x-1])
            dy += 1

        while dx+y < board.shape[1]-1 and board[y, x+dx] != current:
            if y + 1 < board.shape[0]:
                right_options.append(board[y+1,x+dx])
            if y - 1 >= 0:
                right_options.append(board[y-1,x+dx])
            dx += 1
        
        right = min(right_options)
        down = min(down_options)

        if right < down:
            if right < down:
                path.append(board[x+1, y])
                compare(x+1, y)
            elif down < right:
                path.append(board[x, y+1])
                compare(x, y+1)


compare(0,0)
print(path)
print(sum(path))

# Part 2
print("\n\nPART 2:")

