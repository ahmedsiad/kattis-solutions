# ***Fantasy Draft Solution***
# Difficulty: 4.3
# Time Limit: 3 seconds, Memory Limit: 1024 MB
# Acceptance: 36%
# CPU Time: 0.16 s
# Author: Darcy Best
# Source: Rocky Mountain Regional Programming Contest 2019
# Link: https://open.kattis.com/problems/fantasydraft


import sys
import math
import collections
import random
from heapq import heappush, heappop
from functools import reduce
input = sys.stdin.readline
 
ints = lambda: list(map(int, input().split()))

n, k = ints()
prefs = []
for _ in range(n):
    line = input().strip().split()
    d = collections.deque(line[1:])
    prefs.append(d)

players = {}
arr = []
p = int(input())
for _ in range(p):
    nm = input().strip()
    players[nm] = True
    arr.append(nm)

ptr = 0
chosen = [[] for _ in range(n)]
cnt = 0
while cnt < n * k:
    owner = cnt % n
    best = None
    while prefs[owner] and not players[prefs[owner][0]]:
        prefs[owner].popleft()
    if len(prefs[owner]) != 0:
        nm = prefs[owner][0]
        chosen[owner].append(nm)
        players[nm] = False
        prefs[owner].popleft()
    else:
        while not players[arr[ptr]]:
            ptr += 1
        nm = arr[ptr]
        chosen[owner].append(nm)
        players[nm] = False
    cnt += 1

for picks in chosen:
    print(" ".join(picks))


