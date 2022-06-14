# ***Synchronizing Lists Solution***
# Difficulty: 1.6
# Time Limit: 1 second, Memory Limit: 1024 MB
# Acceptance: 61%
# CPU Time: 0.07 s
# Author: Greg Hamerly
# Source: Baylor Competitive Learning course
# Link: https://open.kattis.com/problems/synchronizinglists


import sys
test_cases = list(map(int, map(str.strip, sys.stdin)))
i = 0
while i < len(test_cases) - 1:
   n = test_cases[i]
   i += 1
   list1 = []
   list2 = []
   for j in range(n):
      list1.append(test_cases[i+j])
   i += n
   for j in range(n):
      list2.append(test_cases[i+j])
   i += n
   list1s = sorted(list1)
   list2s = sorted(list2)
   h = {}
   for k in range(n):
      h[list1s[k]] = list2s[k]
   for n in list1:
      print(h[n])
   if i != len(test_cases) - 1: print("")  
    
    
      

