# ***Bitmask Solution***
# Difficulty: 3.4
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 62%
# CPU Time: 0.08 s
# Author: Howard Cheng
# Source: Alberta Collegiate Programming Contest 2021
# Link: https://open.kattis.com/problems/bitmask


import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce
input = sys.stdin.readline
 
ints = lambda: list(map(int, input().split()))

s = input().strip()
n = len(s)
a = ints()

def dfs(i, mp):
    if i == n:
        return 0

    ans = math.inf
    for j in range(n - i):
        t = ""
        for l in range(i, i + j + 1):
            d = 1 - int(s[l])
            t += str(d)
        res = 0
        if t in mp:
            res = dfs(i + j + 1, mp)
        else:
            mp[t] = True
            res = a[j] + dfs(i + j + 1, mp)
            del mp[t]
        ans = min(ans, res)
    return ans

print(dfs(0, {}))
