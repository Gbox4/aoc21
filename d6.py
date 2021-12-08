# Gabe Banks
# 12/6/21
# Advent of Code day 6

data = "1,2,1,3,2,1,1,5,1,4,1,2,1,4,3,3,5,1,1,3,5,3,4,5,5,4,3,1,1,4,3,1,5,2,5,2,4,1,1,1,1,1,1,1,4,1,4,4,4,1,4,4,1,4,2,1,1,1,1,3,5,4,3,3,5,4,1,3,1,1,2,1,1,1,4,1,2,5,2,3,1,1,1,2,1,5,1,1,1,4,4,4,1,5,1,2,3,2,2,2,1,1,4,3,1,4,4,2,1,1,5,1,1,1,3,1,2,1,1,1,1,4,5,5,2,3,4,2,1,1,1,2,1,1,5,5,3,5,4,3,1,3,1,1,5,1,1,4,2,1,3,1,1,4,3,1,5,1,1,3,4,2,2,1,1,2,1,1,2,1,3,2,3,1,4,5,1,1,4,3,3,1,1,2,2,1,5,2,1,3,4,5,4,5,5,4,3,1,5,1,1,1,4,4,3,2,5,2,1,4,3,5,1,3,5,1,3,3,1,1,1,2,5,3,1,1,3,1,1,1,2,1,5,1,5,1,3,1,1,5,4,3,3,2,2,1,1,3,4,1,1,1,1,4,1,3,1,5,1,1,3,1,1,1,1,2,2,4,4,4,1,2,5,5,2,2,4,1,1,4,2,1,1,5,1,5,3,5,4,5,3,1,1,1,2,3,1,2,1,1"

# data = """3,4,3,1,2"""

data = data.split(",")
data = [ int(x) for x in data ]

def calc_children(start_time, days):
  total = 1

  children = int( (days + 7 - start_time) / 7 )

  # total += children

  for i in range(children):
    total += calc_children(8, days - (i) * 7 - start_time - 1)
  
  return total


# Part 1
def p1(data):
  fish = data.copy()

  for t in range(80):
    for i, x in enumerate(fish.copy()):  
      if x == 0:
        fish.append(8)
        fish[i] = 6
      
      else:
        fish[i] -= 1

  print(len(fish))

from collections import deque, Counter

# Part 2
def p2(data):
  fish = []

  for i in range(10):
    fish.append( data.count(i) )
  
  fish = deque(fish)

  days = 256

  for i in range(days):
    fish[9] += fish[0]
    fish[7] += fish[0]
    fish[0] = 0

    fish.rotate(-1)

  print(sum(fish))
  

  
if __name__ == "__main__":
  print("\n\nPART1:")
  p1(data)
  print("\n\nPART2:")
  p2(data)

# its gonna produce: int( (days + 7 - initial start) / 7 )
# Each kid is gonna produce: int( (daysLeft + 7 - 8) / 7 )
#                            int( ((days - 7*i) - 1) / 7 )
