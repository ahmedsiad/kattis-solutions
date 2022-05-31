# ***Greedily Increasing Subsequence Solution***
# Difficulty: 2.0
# Time Limit: 5 seconds, Memory Limit: 1024 MB
# CPU Time: 0.33 s
# Author: Johan Sannemo
# Source: HiQ Challenge 2017
# Link: https://open.kattis.com/problems/greedilyincreasing


n = int(input())
nums = list(map(int, input().split()))
gis = [nums[0]]
for i in range(1, n):
  if nums[i] > gis[-1]:
    gis.append(nums[i])
print(len(gis))
print(" ".join([str(x) for x in gis]))
