***FizzBuzz Solution***
Difficulty: 1.3
Time Limit: 1 second, Memory Limit: 1024 MB
CPU Time: 0.06 s
Author: Darko Aleksic
Source: Rocky Mountain Regional Contest (RMRC) 2016
Link: https://open.kattis.com/problems/fizzbuzz


import sys

for i in sys.stdin:
    ab = i.split()
    x = int(ab[0])
    y = int(ab[1])
    n = int(ab[2])

    for i in range(1, n+1):
        res = ""
        if (i % x == 0): res += "Fizz"
        if (i % y == 0): res += "Buzz"
        if (res == ""): res = str(i)
        print(res)

