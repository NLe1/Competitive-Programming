num = int(input())

while num != -1:
    total = 0
    prev = 0
    for i in range(num):
        v = input().rstrip().split()
        s = int(v[0])
        h = int(v[1])
        total += s * (h-prev)
        prev = h
    print(f'{total} miles')
    num = int(input())