# Gabe Banks
# 12/11/21
# Advent of Code day 12

import numpy as np

data = """vn-DD
qm-DD
MV-xy
end-xy
KG-end
end-kw
qm-xy
start-vn
MV-vn
vn-ko
lj-KG
DD-xy
lj-kh
lj-MV
ko-MV
kw-qm
qm-MV
lj-kw
VH-lj
ko-qm
ko-start
MV-start
DD-ko"""

# data = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end"""

data = data.split("\n")
data = [ x.split("-") for x in data ]
for i in [list(reversed(x)) for x in data]:
    data.append(i)

# Part 1
print("PART 1:")

# [print(x) for x in data]

# print()

paths = 0
def explore(start, current_path):
    global paths
    global seen

    orig = current_path.copy()
    links = list(filter(lambda x: x[0]==start, data))
    for link in links:
        current_path = orig.copy()
        current_path.append(link[1])
        # print(current_path)

        invalid_path = False
        for i in current_path:
            if i.islower() and current_path.count(i) > 1:
                invalid_path = True
        
        if invalid_path:
            continue

        if link[1] == "end":
            # print(current_path)
            paths += 1
            continue
        explore(link[1], current_path.copy())

explore('start', ['start'])
print(paths)
    

# Part 2
print("\n\nPART 2:")

paths = 0
def explore(start, current_path):
    global paths
    global seen

    orig = current_path.copy()
    links = list(filter(lambda x: x[0]==start, data))
    for link in links:
        current_path = orig.copy()
        current_path.append(link[1])
        # print(current_path)

        invalid_path = False
        used_twice = False
        more_than_once = set(list(filter(lambda x: current_path.count(x) > 1, current_path)))
        for i in more_than_once:
            if i.islower():
                visits = current_path.count(i)
                if used_twice == False and visits == 2 and not i in ['start', 'end']:
                    used_twice = True
                else:
                    invalid_path = True
        
        if invalid_path:
            continue

        if link[1] == "end":
            # print(current_path)
            paths += 1
            continue
        explore(link[1], current_path.copy())

explore('start', ['start'])
print(paths)