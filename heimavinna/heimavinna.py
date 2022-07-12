# ***Homework Solution***
# Difficulty: 1.1
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 92%
# CPU Time: 0.04 s
# Author: No author
# Source: No source
# Link: https://open.kattis.com/problems/heimavinna


import sys

total = 0
for i in sys.stdin:
    ab = i.split(';')
    for st in ab:
        s = st.split('-')
        if len(s) > 1:
            total += int(s[1]) - int(s[0])
        total += 1

print(total)
# test 234

