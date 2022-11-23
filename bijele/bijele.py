# ***Bijele Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 60%
# CPU Time: 0.05 s
# Author: No author
# Source: Croatian Open Competition in Informatics 2007/2008, contest #2
# Link: https://open.kattis.com/problems/bijele


a = list(map(int, input().split()))
b = 0
r = [1 - a[0], 1 - a[1], 2 - a[2], 2 - a[3], 2 - a[4], 8 - a[5]]
print(*r)
