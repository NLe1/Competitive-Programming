from collections import Counter
s = input()
c = Counter(list(s))

ans = 0
for (k, v) in c.items():
    ans += v*v

v = c.values()
if len(v) == 3:
    m = min(c.values())
    ans += m * 7

print(ans)