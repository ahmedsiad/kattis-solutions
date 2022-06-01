# ***Verify This, Your Majesty Solution***
# Difficulty: 2.9
# Time Limit: 5 seconds, Memory Limit: 1024 MB
# CPU Time: 0.10 s
# Author: No author
# Source: University of Chicago - Department of Computer Science
# Link: https://open.kattis.com/problems/queens


n = int(input())
rows = {}
cols = {}
diags1 = {}
diags2 = {}

for _ in range(n):
  x, y = list(map(int, input().split()))
  if x in rows or y in cols or x - y in diags1 or x + y in diags2:
    print("INCORRECT")
    break
  rows[x], cols[y], diags1[x - y], diags2[x + y] = [True] * 4
if len(rows) == n:
  print("CORRECT")
