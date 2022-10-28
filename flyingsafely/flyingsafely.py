# ***Flying Safely Solution***
# Difficulty: 1.7
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 63%
# CPU Time: 0.16 s
# Author: No author
# Source: Benelux Algorithm Programming Contest (BAPC) 2013
# Link: https://open.kattis.com/problems/flyingsafely


import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce
input = sys.stdin.readline
 
ints = lambda: list(map(int, input().split()))

class UnionFind:
    def __init__(self, n):
        self.link = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self, a):
        while self.link[a] != a:
            a = self.link[a]
        return a
    
    def same(self, a, b):
        return self.find(a) == self.find(b)
    
    def join(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]
        return b

t = int(input())
for _ in range(t):
    n, m = ints()
    edges = []
    for _ in range(m):
        u, v = ints()
        edges.append((u, v))

    dsu = UnionFind(n + 1)
    ans = 0
    for u, v in edges:
        if not dsu.same(u, v):
            dsu.join(u, v)
            ans += 1 

    print(ans)
