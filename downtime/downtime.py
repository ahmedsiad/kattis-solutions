# ***Disastrous Downtime Solution***
# Difficulty: 2.9
# Time Limit: 2 seconds, Memory Limit: 1024 MB
# CPU Time: 0.17 s
# Author: Oskar Werkelin Ahlin
# Source: Nordic Collegiate Programming Contest (NCPC) 2015
# Link: https://open.kattis.com/problems/downtime


import math
n, k = list(map(int, input().split()))
ts = []
for _ in range(n): ts.append(int(input()))

max_overlap = 0
i, j = 0, 1
while i < n:
  while j < n and ts[j] < ts[i] + 1000:
    j += 1
  max_overlap = max(max_overlap, j - i)
  i += 1

ans = math.ceil(max_overlap / k)  
print(ans)
