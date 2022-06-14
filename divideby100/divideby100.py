# ***Divide by 100... Solution***
# Difficulty: 4.2
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 30%
# CPU Time: 0.15 s
# Author: Modan Han
# Source: Alberta Collegiate Programming Contest 2017
# Link: https://open.kattis.com/problems/divideby100


n = input()
m = input()
nl = len(n)
ml = len(m)

ans = []

if nl >= ml:
  dc = nl - ml + 1
  for i in range(nl):
    if dc == i:
      ans.append(".")
      break
    ans.append(n[i])
  stop = dc
  for i in range(nl - 1, dc, -1):
    if n[i] != "0":
      stop = i + 1
      break
  for i in range(dc, stop):
    ans.append(n[i])
  if ans[-1] == ".": ans.pop()
else:
  ans.append("0")
  ans.append(".")
  
  for i in range(ml - nl - 1):
    ans.append("0")
  for i in range(nl):
    ans.append(n[i])

print("".join(ans))
# amazing problem!!
  

