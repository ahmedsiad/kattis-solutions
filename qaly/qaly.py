# ***Quality-Adjusted Life-Year Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.06 s
# Author: Howard Cheng
# Source: Rocky Mountain Regional Programming Contest 2018
# Link: https://open.kattis.com/problems/qaly


n = int(input())
s = 0
for _ in range(n):
  a, b = list(map(float, input().split()))
  s += a * b
print(s)
