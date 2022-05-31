# ***Mastering Mastermind Solution***
# Difficulty: 2.6
# Time Limit: 1 second, Memory Limit: 2048 MB
# CPU Time: 0.05 s
# Author: John Bonomo
# Source: 2015 ICPC East-Central NA Regional Contest Practice Session
# Link: https://open.kattis.com/problems/mastermind


n, s1, s2 = input().split()
n = int(n)

r1, r2 = "", ""
r = 0
s = 0

for i in range(n):
  if s1[i] == s2[i]: r += 1
  else:
    r1 += s1[i]
    r2 += s2[i]

r1 = sorted(r1)
r2 = sorted(r2)

j = 0
for i in range(len(r1)):
  while j < len(r1) and ord(r2[j]) <= ord(r1[i]):
    if r1[i] == r2[j]:
      s += 1
      j += 1
      break
    j += 1
print(r, s)
