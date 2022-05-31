# ***Pivot Solution***
# Difficulty: 2.8
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.10 s
# Author: Steven Halim
# Source: ICPC SG Preliminary Contest 2015
# Link: https://open.kattis.com/problems/pivot


n = int(input())
a = list(map(int, input().split()))
right = sorted(a[1:])
visited = set()
total = 0
left = a[0]

if a[0] < right[0]: total += 1
i = 0
for num in a:
  while i < n - 1 and right[i] in visited:
    i += 1
  if i == n - 1: break
  if left < num < right[i]:
    total += 1
  left = max(left, num)
  visited.add(right[i])
if a[-1] > max(sorted(a[0:n-1])): total += 1
print(total) 
