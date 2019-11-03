import sys
import random
import time


# i,j is inclusive
def getMin(items, i, j, dividers, d):
    if i == j: dividers = 0
    if f'{i}_{j}_{dividers}' in d.keys(): return d[f'{i}_{j}_{dividers}']
    if dividers == 0 or i == j:
        sum = 0
        for x in range(i, j + 1):
            sum += items[x]
        if sum % 10 >= 5:
            sum = (int(sum / 10) + 1) * 10
        else:
            sum = int(sum / 10) * 10
        d[f'{i}_{j}_{0}'] = sum
        return sum
    else:
        m = sys.maxsize
        for x in range(i, j):
            # divided
            t1 = getMin(items, i, x, dividers - 1, d)
            t2 = getMin(items, x + 1, j, dividers - 1, d)
            temp = t1 + t2
            if i != x:
                d[f'{i}_{x}_{dividers - 1}'] = t1
            if x + 1 != j:
                d[f'{x + 1}_{j}_{dividers - 1}'] = t2
            if temp < m: m = temp
        d[f'{i}_{j}_{dividers}'] = m

    return m


# s = input().rstrip().split()
# num = int(s[0])
# dividers = int(s[1])
#
# s = input().rstrip().split()
# s = [int(x) for x in s]
d = dict()
test = []
for x in range(2000):
    test.append(random.randint(0,10000))

a = time.time()
print(getMin(test, 0, len(test) - 1, random.randint(15,20), d))
print(time.time() - a)
print(d)
