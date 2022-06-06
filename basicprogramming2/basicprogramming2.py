# ***Basic Programming 2 Solution***
# Difficulty: 2.6
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.11 s
# Author: Sample data files
# Source: Steven Halim
# Link: https://open.kattis.com/problems/basicprogramming2


n, t = list(map(int, input().split()))
nums = sorted(list(map(int, input().split())))

if t == 1:
  i = 0
  j = n - 1
  flag = False
  while i < j:
    sm = nums[i] + nums[j]
    if sm == 7777:
      flag = True
      break
    elif sm > 7777:
      j -= 1
    else: i += 1
  print("Yes") if flag else print("No")
elif t == 2:
  flag = False
  for i in range(1, n):
    if nums[i] == nums[i - 1]:
      flag = True
      break
  print("Contains duplicate") if flag else print("Unique")
elif t == 3:
  occ = 0
  curr = nums[0]
  flag = False
  for i in range(n):
    if nums[i] != curr:
      curr = nums[i]
      occ = 0
    else:
      occ += 1
      if occ > n // 2:
        flag = True
        break
  print(curr) if flag else print("-1")
elif t == 4:
  if n % 2 == 0:
    print(nums[n // 2 - 1], nums[n // 2])
  else:
    print(nums[n // 2])
else:
  l = [str(x) for x in nums if 100 <= x <= 999]
  print(" ".join(l))
