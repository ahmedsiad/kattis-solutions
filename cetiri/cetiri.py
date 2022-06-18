# ***Cetiri Solution***
# Difficulty: 1.7
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 55%
# CPU Time: 0.04 s
# Author: No author
# Source: Croatian Open Competition in Informatics 2007/2008, contest #3
# Link: https://open.kattis.com/problems/cetiri


li = list(map(int, input().split()))
li = sorted(li)
d1 = li[1] - li[0]
d2 = li[2] - li[1]
if d1 == d2:
  print(li[2] + d2)
elif d1 < d2:
  print(li[1] + d1)
else:
  print(li[0] + d2)
