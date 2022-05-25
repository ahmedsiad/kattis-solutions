# ***Finding An A Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Zachary Friggstad
# Source: Alberta Collegiate Programming Contest 2021
# Link: https://open.kattis.com/problems/findingana


s = input()
for i in range(len(s)):
  if s[i] == "a":
    print(s[i:])
    break

