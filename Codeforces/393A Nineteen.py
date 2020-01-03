from collections import Counter

s = [ch for ch in input()]
c = Counter(s)
# 3n,1i,1t,3e

print(min(int(c.get('n', 0) / 3), int(c.get('e', 0) / 3), c.get('i', 0), c.get('t', 0)))
