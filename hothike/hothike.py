# ***Hot Hike Solution***
# Difficulty: 2.1
# Time Limit: 2 seconds, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Per Austrin
# Source: Nordic Collegiate Programming Contest (NCPC) 2019
# Link: https://open.kattis.com/problems/hothike


n = int(input())
days = list(map(int, input().split()))
d, t = 0, 41
for i in range(n - 2):
  if max(days[i], days[i+2]) < t:
    d, t = i + 1, max(days[i], days[i+2])
print(d, t)
