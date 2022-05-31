# ***Erase Securely Solution***
# Difficulty: 1.8
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Ulf Lundström
# Source: Nordic Collegiate Programming Contest (NCPC) 2013
# Link: https://open.kattis.com/problems/erase


n = int(input())
l1 = input()
l2 = input()
if n % 2 == 0:
  if l1 == l2: print("Deletion succeeded")
  else: print("Deletion failed")
else:
  flag = False
  for i in range(len(l1)):
    if l1[i] == l2[i]:
      flag = True
      break
  if flag: print("Deletion failed")
  else: print("Deletion succeeded")
