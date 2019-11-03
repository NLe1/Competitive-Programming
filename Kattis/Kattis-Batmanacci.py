def p(n, k, d):
    while True:
        if n == 1: return 'N'
        if n == 2: return 'A'
        lower = d[n-2]
        if k <= lower:
            n -= 2
        else:
            n-=1
            k-=lower

def getFib(n, d):
    for x in range(3, n+1):
        d[x] = d[x-1] + d[x-2]

s = input().split()
n = int(s[0])
d = {1:1, 2:1}
getFib(n,d)
k = int(s[1])
print(p(n,k,d))