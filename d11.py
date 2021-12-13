# Gabe Banks
# 12/10/21
# Advent of Code day 11

import numpy as np

data = """4575355623
3325578426
7885165576
4871455658
3722545312
8362663832
5562743324
4165776412
1817813675
4255524632"""

# data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""

data = data.split("\n")
data = [ [int(y) for y in x ] for x in data ]
data = np.array(data)

# Part 1
print("PART 1:")

def flashing():
    a = data > 9
    if len(list(zip(*np.nonzero(a)))) > 0:
        return True
    else:
        return False

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', -9999)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value

data = np.pad(data, 1, pad_with)

flashes = 0
for step in range(100):
    data += 1
    already_flashed = []
    while flashing():
        a = data > 9
        flashpos = list(zip(*np.nonzero(a)))
        for flash in flashpos:
            if flash in already_flashed:
                data[flash[0], flash[1]] = 0
                continue
            flashes += 1
            already_flashed.append(flash)
            b = data[flash[0]-1:flash[0]+2, flash[1]-1:flash[1]+2]
            data[flash[0]-1:flash[0]+2, flash[1]-1:flash[1]+2] += 1
            data[flash[0], flash[1]] = 0
    
    for flash in already_flashed:
        data[flash[0], flash[1]] = 0


print(flashes)

# Part 2
print("\n\nPART 2:")

while np.sum(data[1:-1, 1:-1]) > 0:
    step += 1
    data += 1
    already_flashed = []
    while flashing():
        a = data > 9
        flashpos = list(zip(*np.nonzero(a)))
        for flash in flashpos:
            if flash in already_flashed:
                data[flash[0], flash[1]] = 0
                continue
            flashes += 1
            already_flashed.append(flash)
            b = data[flash[0]-1:flash[0]+2, flash[1]-1:flash[1]+2]
            data[flash[0]-1:flash[0]+2, flash[1]-1:flash[1]+2] += 1
            data[flash[0], flash[1]] = 0
    
    for flash in already_flashed:
        data[flash[0], flash[1]] = 0

print(step)