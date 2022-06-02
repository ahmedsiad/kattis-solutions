# ***This Ain't Your Grandpa's Checkerboard Solution***
# Difficulty: 1.8
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.06 s
# Author: No author
# Source: ICPC North America Regional Contests 2019-11-09
# Link: https://open.kattis.com/problems/thisaintyourgrandpascheckerboard


n = int(input())
grid = []
for _ in range(n):
  grid.append(list(input()))

flag = False
for i in range(n):
  b, w = 0, 0
  c = [0, 0]
  for j in range(n):
    if grid[i][j] == "B":
      b += 1
      c[1] += 1
      if c[0] == 1:
        c = [0, 1]
      if c[1] == 3: flag = True
    else:
      w += 1
      c[1] += 1
      if c[0] == 0:
        c = [1, 1]
      if c[1] == 3: flag = True
  if b != w: flag = True
for i in range(n):
  b, w = 0, 0
  c = [0, 0]
  for j in range(n):
    if grid[j][i] == "B":
      b += 1
      c[1] += 1
      if c[0] == 1:
        c = [0, 1]
      if c[1] == 3: flag = True
    else:
      w += 1
      c[1] += 1
      if c[0] == 0:
        c = [1, 1]
      if c[1] == 3: flag = True
  if b != w: flag = True
if flag: print("0")
else: print("1")
