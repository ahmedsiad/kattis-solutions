# ***Speed Limit Solution***
# Difficulty: 1.5
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: John Cigas
# Source: 2004 ACM ICPC Mid-Central North American Regional Contest
# Link: https://open.kattis.com/problems/speedlimit



while True:
  n = int(input())
  if n == -1: break
  total = 0
  last = 0
  for _ in range(n):
    s, h = list(map(int, input().split()))
    total += s * (h - last)
    last = h
  print(str(total) + " miles")
