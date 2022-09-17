# ***10 Kinds of People Solution***
# Difficulty: 5.2
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 20%
# CPU Time: 0.38 s
# Author: David Sturgill
# Source: Baylor Competitive Learning course
# Link: https://open.kattis.com/problems/10kindsofpeople


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

r, c = ints()
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
graph = []
for _ in range(r):
    graph.append(input().strip())
dsu = UnionFind(r * c)

for i in range(r):
    for j in range(c):
        for d in dirs:
            ni, nj = i + d[0], j + d[1]
            if not 0 <= ni < r or not 0 <= nj < c: continue
            if graph[i][j] != graph[ni][nj]: continue
            a = i * c + j
            b = ni * c + nj
            if not dsu.same(a, b):
                dsu.join(a, b)

n = int(input())
for _ in range(n):
    r1, c1, r2, c2 = ints()
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    a, b = r1 * c + c1, r2 * c + c2
    if graph[r1][c1] != graph[r2][c2] or not dsu.same(a, b):
        print("neither")
    else:
        if graph[r1][c1] == "0":
            print("binary")
        else:
            print("decimal")



