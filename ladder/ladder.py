# ***Ladder Solution***
# Difficulty: 1.4
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Per Austrin
# Source: Spotify Challenge 2010
# Link: https://open.kattis.com/problems/ladder


import math

i = input().split()
h, v = int(i[0]), int(i[1])
ans = math.ceil(h / math.sin(v * math.pi / 180))
print(str(ans))
