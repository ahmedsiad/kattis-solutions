# ***Basketball One-on-One Solution***
# Difficulty: 1.6
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Jingbo Shang
# Source: 2019 ICPC Mid-Central Regional
# Link: https://open.kattis.com/problems/basketballoneonone


s = input()
a = 0
b = 0
for i in range(0, len(s), 2):
  if s[i] == "A": a += int(s[i+1])
  else: b += int(s[i+1])
if a > b: print("A")
else: print("B")
