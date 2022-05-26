# ***Pot Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Nikola Dmitrović
# Source: Croatian Open Competition in Informatics 2015/2016, contest #3
# Link: https://open.kattis.com/problems/pot


n = int(input())
s = 0
for _ in range(n):
  b = input()
  p = int(b[-1])
  x = int(b[:-1])
  s += x ** p
print(s)
