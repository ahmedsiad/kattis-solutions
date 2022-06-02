# ***Flow Shop Solution***
# Difficulty: 2.2
# Time Limit: 3 seconds, Memory Limit: 1024 MB
# CPU Time: 0.18 s
# Author: Zachary Friggstad
# Source: Rocky Mountain Regional Contest (RMRC) 2016
# Link: https://open.kattis.com/problems/flowshop


n, m = list(map(int, input().split()))

grid = []
for _ in range(n):
  grid.append(list(map(int, input().split())))

for i in range(1, m):
  grid[0][i] += grid[0][i - 1]

res = [str(grid[0][-1])]
for i in range(1, n):
  for j in range(m):
    if j > 0 and grid[i][j - 1] > grid[i - 1][j]:
      grid[i][j] += grid[i][j - 1]
    else:
      grid[i][j] += grid[i - 1][j]
  res.append(str(grid[i][-1]))

print(" ".join(res))
