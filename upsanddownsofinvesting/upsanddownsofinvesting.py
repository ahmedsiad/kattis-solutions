# ***The Ups and Downs of Investing Solution***
# Difficulty: 3.4
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.06 s
# Author: John Bonomo
# Source: 2018 ICPC East-Central NA Regional Practice Contest
# Link: https://open.kattis.com/problems/upsanddownsofinvesting


import sys
s, n, m = list(map(int, input().split()))

stocks = []
for i in sys.stdin:
  l = list(map(int, i.split()))
  stocks.extend(l)
peaks = 0
i = 0
c = 1
while i < s - 1:
  if stocks[i] < stocks[i + 1]:
    c += 1
  else:
    d = 1
    while i < s - 1 and stocks[i + 1] < stocks[i]:
      d, i = d + 1, i + 1
    if c >= n and d >= n:
      peaks += 1
    c = 1
    i -= 1
  i += 1

valleys = 0
i = 0
c = 1
while i < s - 1:
  if stocks[i] > stocks[i + 1]:
    c += 1
  else:
    d = 1
    while i < s - 1 and stocks[i + 1] > stocks[i]:
      d, i = d + 1, i + 1
    if c >= m and d >= m:
      valleys += 1
    c = 1
    i -= 1
  i += 1

print(peaks, valleys)
