# ***Bumper-To-Bumper Traffic Solution***
# Difficulty: 4.1
# Time Limit: 3 seconds, Memory Limit: 1024 MB
# CPU Time: 0.15 s
# Author: Zachary Friggstad
# Source: Rocky Mountain Regional Contest (RMRC) 2016
# Link: https://open.kattis.com/problems/traffic


p1, p2 = list(map(int, input().split()))

t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

t = 1
i = 1
j = 1
while t < 3000002:
  if i <= t1[0] and t >= t1[i]:
    i += 1
  if j <= t2[0] and t >= t2[j]:
    j += 1

  if i % 2 == 0:
    p1 += 1
  if j % 2 == 0:
    p2 += 1

  if abs(p1 - p2) < 5:
    print("bumper tap at time " + str(t + 1))
    break
  t += 1

if abs(p1 - p2) >= 5:
  print("safe and sound")
