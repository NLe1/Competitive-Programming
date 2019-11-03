n = int(input())

while n != 0:
    d = dict()

    for i in range(n):
        s = input()
        if s[0:2] in d:
            d[s[0:2]].append(s)
        else:
            d[s[0:2]] = [s]

    for key, value in sorted(d.items()):
        print(*value, sep="\n")

    n = int(input())

    if n != 0:
        print()