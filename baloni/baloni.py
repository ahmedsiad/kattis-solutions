# ***Baloni Solution***
# Difficulty: 3.1
# Time Limit: 4 seconds, Memory Limit: 1024 MB
# CPU Time: 0.25 s
# Author: Dominik Gleich
# Source: Croatian Open Competition in Informatics 2015/2016, contest #1
# Link: https://open.kattis.com/problems/baloni


import collections

n = int(input())
heights = list(map(int, input().split()))
arrows = collections.defaultdict(int)
arrows[heights[0] - 1] = True
total = 1

for i in range(1, n):
  h = heights[i]
  if arrows[h] > 0:
    arrows[h] -= 1
  else:
    total += 1
  arrows[h - 1] += 1

print(total)
