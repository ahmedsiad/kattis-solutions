# ***Quadrant Selection Solution***
# Difficulty: 1.2
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: No author
# Source: Canadian Computing Competition 2017
# Link: https://open.kattis.com/problems/quadrant


x = int(input())
y = int(input())

if x > 0 and y > 0:
  print("1")
elif x < 0 and y < 0:
  print("3")
elif x > 0 and y < 0:
  print("4")
else:
  print("2")
