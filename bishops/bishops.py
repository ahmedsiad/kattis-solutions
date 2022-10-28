# ***Bishops Solution***
# Difficulty: 2.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 39%
# CPU Time: 0.05 s
# Author: No author
# Source: IPSC 2004
# Link: https://open.kattis.com/problems/bishops


import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce
input = sys.stdin.readline
 
ints = lambda: list(map(int, input().split()))

while True:
    try:
        n = int(input())
        print(max(n * 2 - 2, 1))
    except:
        break
