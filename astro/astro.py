# ***Astro Solution***
# Difficulty: 3.8
# Time Limit: 1 second, Memory Limit: 1024 MB
# CPU Time: 0.07 s
# Author: Adrian Satja Kurdija
# Source: Croatian Open Competition in Informatics 2010/2011, contest #4
# Link: https://open.kattis.com/problems/astro


s1 = list(map(int, input().split(":")))
s2 = list(map(int, input().split(":")))
f1 = list(map(int, input().split(":")))
f2 = list(map(int, input().split(":")))

flashes = [(0, s1)]
for i in range(1441):
  f = flashes[-1][1].copy()
  f[1] += f1[1]
  f[0] += f1[0]
  if f[1] >= 60:
    f[0] += 1
    f[1] -= 60
  days = flashes[-1][0]
  if f[0] >= 24:
    f[0] -= 24
    days += 1
  flashes.append((days, f))

i = 0
f3 = [0, s2.copy()]
flag = False
while i < len(flashes):
  tm1 = flashes[i][0] * 24 * 60 + flashes[i][1][0] * 60 + flashes[i][1][1]
  tm2 = f3[0] * 24 * 60 + f3[1][0] * 60 + f3[1][1]
  if tm1 < tm2:
    i += 1
  elif tm1 > tm2:
    f3[1][0] += f2[0]
    f3[1][1] += f2[1]
    if f3[1][1] >= 60:
      f3[1][0] += 1
      f3[1][1] -= 60
    days = f3[0]
    if f3[1][0] >= 24:
      f3[1][0] -= 24
      days += 1
    f3[0] = days
  else:
    flag = True
    break

days = ["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if flag:
  day = f3[0] % 7
  print(days[day])
  ans = "" + str(f3[1][0])
  if f3[1][0] < 10:
    ans = "0" + ans
  ans = ans + ":"
  if f3[1][1] < 10:
    ans = ans + "0"
  ans = ans + str(f3[1][1])
  print(ans)
else: print("Never")

