import sys

probs = []

for i in sys.stdin:
    ab = i.split()
    if len(ab) == 1: continue
    x = ab[0]
    y = ab[1]

    probs.append(float(y))

total = 0
probs.sort(reverse=True)

for i in range(len(probs)):
    total += (i + 1) * probs[i]

print(total)



