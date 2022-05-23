# ***Odd Echo Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.06 s
# Author: Johan Sannemo
# Source: Principles of Algorithmic Problem Solving
# Link: https://open.kattis.com/problems/oddecho


N = int(input())

flag = True
for _ in range(N):
  word = input()
  if flag: print(word)
  flag = not flag

