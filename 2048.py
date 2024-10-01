import random

w, h = 4, 4

Matrix = [[0 for x in range(w)] for y in range (h)]

def new_number():
  x = random.randint(0,3)
  y = random.randint(0,3)
  if Matrix[x][y] == 0:
    Matrix[x][y] = 2
  else:
    new_number()

# Prints matrix with seperator
def print_matrix():
  for y in range (4):
    print(Matrix[0][y], Matrix[1][y], Matrix[2][y], Matrix[3][y])
  print("-=-=-=-")

# 1 is up, 2 is, right, 3 is down, 4 is left
def move(x):
  if x == 1:

  elif x == 2:
  elif x == 3:
  elif x == 4:
