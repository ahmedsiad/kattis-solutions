# ***EpigDanceOff Solution***
# Difficulty: 1.9
# Time Limit: 2 seconds, Memory Limit: 1024 MB
# CPU Time: 0.29 s
# Author: Anthony Han
# Source: Calgary Collegiate Programming Contest 2019
# Link: https://open.kattis.com/problems/epigdanceoff


n, m = list(map(int, input().split()))

grid = []
for _ in range(n):
  grid.append(list(input()))

count = 1
for i in range(m):
  flag = False
  for j in range(n):
    if grid[j][i] == "$": flag = True
  if not flag:
    count += 1
print(count)
