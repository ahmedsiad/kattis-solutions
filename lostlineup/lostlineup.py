# ***Lost Lineup Solution***
# Difficulty: 1.5
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.06 s
# Author: Brandon Fuller
# Source: Rocky Mountain Regional Programming Contest 2019
# Link: https://open.kattis.com/problems/lostlineup


n = int(input())
ppl = list(map(int, input().split()))
res = [1] * n
for i,d in enumerate(ppl):
  res[d+1] = i + 2
k = " ".join([str(x) for x in res])
print(k)
