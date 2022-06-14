# ***Sort Two Numbers Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 54%
# CPU Time: 0.04 s
# Author: Greg Hamerly
# Source: Kattis
# Link: https://open.kattis.com/problems/sorttwonumbers


a, b = list(map(int, input().split()))
if a < b:
    print(a, b)
else:
    print(b, a)
