n = int(input())
items = []
p1 = []
p2 = []
se = []
for i in range(n):
    items.append(input())

m = int(input())
for i in range(m):
    s = input().rstrip().split()
    if s[0] not in p1 and s[1] not in p2:
        p1.append(s[0])
        p2.append(s[1])
    elif s[0] in p1 and s[1] not in p2:
        p2.append(s[1])
    elif s[0] not in p1 and s[1] in p2:
        p1.append(s[0])
    se.append((s[0],s[1]))

print(se)
print(items)

