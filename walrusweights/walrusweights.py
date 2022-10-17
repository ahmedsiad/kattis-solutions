# ***Walrus Weights Solution***
# Difficulty: 4.1
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 30%
# CPU Time: 0.09 s
# Author: Marc Vinyals
# Source: Popup 2015 Session 1
# Link: https://open.kattis.com/problems/walrusweights


n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))
    
dp = [False] * 2001
dp[0] = True

ans = 0
for i in range(n):
    for j in range(2000, -1, -1):
        if j - a[i] >= 0 and dp[j - a[i]]:
            dp[j] = True
            if abs(1000 - ans) > abs(1000 - j):
                ans = j
            elif abs(1000 - ans) == abs(1000 - j) and j > ans:
                ans = j

print(ans)
