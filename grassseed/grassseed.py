# ***Grass Seed Inc. Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Sample data files
# Source: Jim Grimmett
# Link: https://open.kattis.com/problems/grassseed


c = float(input())
l = int(input())
total = 0
for _ in range(l):
    a, b = list(map(float, input().split()))
    total += a * b * c
print(total)
