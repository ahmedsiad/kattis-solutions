# ***Nine Knights Solution***
# Difficulty: 1.9
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: R. Marshall
# Source: 2017 ICPC Mid-Central Regional
# Link: https://open.kattis.com/problems/nineknights


grid = []
for _ in range(5):
  grid.append(list(input()))


flag = True
count = 0
for i in range(5):
  for j in range(5):
    if grid[i][j] == "k":
      count += 1
      if i - 1 > -1 and j - 2 > -1 and grid[i-1][j-2] == "k":
        flag = False
      if i - 2 > -1 and j - 1 > -1 and grid[i-2][j-1] == "k":
        flag = False
      if i - 1 > -1 and j + 2 < 5 and grid[i-1][j+2] == "k":
        flag = False
      if i - 2 > -1 and j + 1 < 5 and grid[i-2][j+1] == "k":
        flag = False
      if i + 1 < 5 and j + 2 < 5 and grid[i+1][j+2] == "k":
        flag = False
      if i + 2 < 5 and j + 1 < 5 and grid[i+2][j+1] == "k":
        flag = False
      if i + 1 < 5 and j - 2 > -1 and grid[i+1][j-2] == "k":
        flag = False
      if i + 2 < 5 and j - 1 > -1 and grid[i+2][j-1] == "k":
        flag = False
if flag and count == 9: print("valid")
else: print("invalid")
