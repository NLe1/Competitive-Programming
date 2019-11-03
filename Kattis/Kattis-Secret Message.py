import math

case = int(input())
for i in range(case):
    s = input()
    l = len(s)
    r = int(math.sqrt(l - 1)) + 1
    ans = ""
    for i in range(r):
        t = ""
        for j in range(i, l, r):
            t += s[j]
        ans += t[::-1]

    print(ans)