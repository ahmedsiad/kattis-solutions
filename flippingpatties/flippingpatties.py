# ***Flipping Patties Solution***
# Difficulty: 2.2
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.06 s
# Author: Arnav Sastry
# Source: ICPC North America Regional Contests 2019-11-09
# Link: https://open.kattis.com/problems/flippingpatties


import collections
import math
n = int(input())

h = collections.defaultdict(int)
mx = 0
for _ in range(n):
  d, t = list(map(int,input().split()))
  h[t] += 1
  h[t - d] += 1
  h[t - 2 * d] += 1
  mx = max(mx, h[t], h[t-d], h[t-2*d])
print(math.ceil(mx/2))
