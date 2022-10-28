# ***Reachable Roads Solution***
# Difficulty: 2.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 50%
# CPU Time: 0.13 s
# Author: Greg Hamerly
# Source: Baylor Competitive Learning course
# Link: https://open.kattis.com/problems/reachableroads


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
    m = int(input())
    edges = []
    r = int(input())
    for _ in range(r):
        u, v = ints()
        edges.append((u, v))

    dsu = UnionFind(m)
    for u, v in edges:
        dsu.join(u, v)
    
    cnt = 0
    for i in range(m):
        if dsu.link[i] == i:
            cnt += 1
    print(cnt - 1)
    
