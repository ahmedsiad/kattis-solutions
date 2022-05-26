# ***Tarifa Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Nikola Dmitrović
# Source: Croatian Open Competition in Informatics 2016/2017, contest #1
# Link: https://open.kattis.com/problems/tarifa


x = int(input())
n = int(input())
s = 0
for _ in range(n):
  s += int(input())
print(x * (n+1) - s)
