***Stacking Cups Solution***
Difficulty: 1.6
Time Limit: 1 second, Memory Limit: 1024 MB
CPU Time: 0.05 s
Author: Darko Aleksic
Source: Rocky Mountain Regional Contest (RMRC) 2016
Link: https://open.kattis.com/problems/cups


import sys

cups = []

for i in sys.stdin:
    ab = i.split()
    if len(ab) == 1: continue
    x = ab[0]
    y = ab[1]

    if x.isnumeric():
        cups.append((int(x)/2, y))
    else: cups.append((int(y), x))


cups.sort()
for cp in cups:
   print(cp[1])
