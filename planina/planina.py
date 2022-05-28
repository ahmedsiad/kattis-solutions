# ***Planina Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Marko Ivanković
# Source: Croatian Open Competition in Informatics 2009/2010, contest #4
# Link: https://open.kattis.com/problems/planina


n = int(input())
ans = 4
last = 4
for i in range(1, n+1):
  l = 2 ** i + 1
  ans += l * l - last
  last = ans
print(ans)
