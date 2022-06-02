# ***Rock Band Solution***
# Difficulty: 4.1
# Time Limit: 4 seconds, Memory Limit: 1024 MB
# CPU Time: 0.42 s
# Author: Josse van Dobben de Bruyn
# Source: Benelux Algorithm Programming Contest (BAPC) preliminaries 2016
# Link: https://open.kattis.com/problems/rockband


m, s = list(map(int, input().split()))
grid = []

for _ in range(m):
  l = list(map(int, input().split()))
  grid.append(l)

songs = {}
for i in range(m):
  songs[grid[i][0]] = True

if len(songs) == 1:
  print("1")
  print(grid[0][0])
else:
  for i in range(1, s):
    all_satisfied = True
    for j in range(m):
      if grid[j][i] not in songs:
        songs[grid[j][i]] = True
      if i + 1 != len(songs):
        all_satisfied = False
    if all_satisfied:
      sgs = sorted(songs.keys())
      print(len(sgs))
      print(" ".join([str(x) for x in sgs]))
      break
