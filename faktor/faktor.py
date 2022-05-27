# ***Faktor Solution***
# Difficulty: 1.3
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.05 s
# Author: Marko Ivanković
# Source: Croatian Open Competition in Informatics 2009/2010, contest #2
# Link: https://open.kattis.com/problems/faktor


a, i = list(map(int, input().split()))
ans = a * (i - 1) + 1
print(ans) 
