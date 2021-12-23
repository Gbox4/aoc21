# Gabe Banks
# 12/13/21
# Advent of Code day 14

import collections
import numpy as np

data = """KOKHCCHNKKFHBKVVHNPN

BN -> C
OS -> K
BK -> C
KO -> V
HF -> K
PS -> B
OK -> C
OC -> B
FH -> K
NV -> F
HO -> H
KK -> H
CV -> P
SC -> C
FK -> N
VV -> F
FN -> F
KP -> O
SB -> O
KF -> B
CH -> K
VF -> K
BH -> H
KV -> F
CO -> N
PK -> N
NH -> P
NN -> C
PP -> H
SH -> N
VO -> O
NC -> F
BC -> B
HC -> H
FS -> C
PN -> F
CK -> K
CN -> V
HS -> S
CB -> N
OF -> B
OV -> K
SK -> S
HP -> C
SN -> P
SP -> B
BP -> C
VP -> C
BS -> K
FV -> F
PH -> P
FF -> P
VK -> F
BV -> S
VB -> S
BF -> O
BB -> H
OB -> B
VS -> P
KB -> P
SF -> N
PF -> S
HH -> P
KN -> K
PC -> B
NB -> O
VC -> P
PV -> H
KH -> O
OP -> O
NF -> K
HN -> P
FC -> H
PO -> B
OH -> C
ON -> N
VN -> B
VH -> F
FO -> B
FP -> B
BO -> H
CC -> P
CS -> K
NO -> V
CF -> N
PB -> H
KS -> P
HK -> S
HB -> K
HV -> O
SV -> H
CP -> S
NP -> N
FB -> B
KC -> V
NS -> P
OO -> V
SO -> O
NK -> K
SS -> H"""

# data = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

from collections import Counter
ITERATIONS = 4

data = data.split("\n")

strand = data[0]

instructions = [ x.split(" -> ") for x in data[2:]]
instructions = dict(instructions)

# Part 1
print("PART 1:")
# print(strand)
# print(instructions)

for x in range(10):
    insert_indexes = []
    insert_values = []
    insert_offset = 0

    for i, c in enumerate(strand[:-1]):
        pair = c + strand[i+1]
        if pair in instructions.keys():
            insert_indexes.append(i+1)
            insert_values.append(instructions[pair])
    
    # print(insert_values)
    # print(insert_indexes)

    for i, val in enumerate(insert_values):
        strand = strand[:insert_indexes[i] + insert_offset] + val + strand[insert_indexes[i] + insert_offset:]
        insert_offset += 1

# print(strand)
# print(len(strand))

maxC = 0
minC = 999999999
for c in set(strand):
    maxC = max(maxC, strand.count(c))
    minC = min(minC, strand.count(c))

print(maxC - minC)

# Part 2

print("\n\nPART 2:")
strand = data[0]
pairs = []
for i, c in enumerate(strand[:-1]):
    pair = c + strand[i+1]
    if pair in instructions.keys():
        pairs.append(pair)


pair_counts = Counter(pairs)
next_pair_counts = pair_counts.copy()

char_counts = Counter(strand)
for i in range(40):
    for k, v in instructions.items():
        occ = pair_counts[k]
        next_pair_counts[k] -= occ
        next_pair_counts[k[0]+v] += occ
        next_pair_counts[v+k[1]] += occ
        char_counts[v] += occ

    pair_counts = next_pair_counts.copy()

pair_counts = {x: count for x, count in pair_counts.items() if count >= 1}

print(max(char_counts.values()) - min(char_counts.values()))
