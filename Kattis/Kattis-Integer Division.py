from collections import Counter
s = input().rstrip().split()
n = int(s[0])
d = int(s[1])
ans = [int(int(x)/d) for x in input().split()]
c = Counter(ans)
count = 0
for c,v in c.items():
    count += int(v*(v-1)/2)

print(count)