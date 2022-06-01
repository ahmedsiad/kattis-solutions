# ***Inverted Deck Solution***
# Difficulty: 4.0
# Time Limit: 4 seconds, Memory Limit: 1024 MB
# CPU Time: 0.36 s
# Author: Robin Lee
# Source: Northwestern Europe Regional Contest (NWERC) 2019
# Link: https://open.kattis.com/problems/inverteddeck


n = int(input())
nums = list(map(int, input().split()))
snums = sorted(nums)

a = -1
b = -1
for i in range(n):
  if a == -1 and nums[i] != snums[i]:
    a = i
  elif nums[i] != snums[i]:
    b = i
if a != -1:
  nums[a:b+1] = reversed(nums[a:b+1])
  if nums == snums:
    print(a+1, b+1)
  else:
    print("impossible")
else:
  print("1 1")
