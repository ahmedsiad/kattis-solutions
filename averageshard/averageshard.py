# ***Paradox With Averages (Hard) Solution***
# Difficulty: 2.8
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 44%
# CPU Time: 0.14 s
# Author: Michal Forišek
# Source: IPSC 2007
# Link: https://open.kattis.com/problems/averageshard


import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce
input = sys.stdin.readline
 
ints = lambda: list(map(int, input().split()))

t = int(input())
for _ in range(t):
    input()
    n, m = ints()
    cs = ints()
    ec = ints()
    avg1 = sum(cs) / n
    avg2 = sum(ec) / m
    ans = 0
    for i in range(n):
        if cs[i] < avg1 and cs[i] > avg2:
            ans += 1
    print(ans)
