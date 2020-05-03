cases = int(input())
def findMax(stack, curIndex, left, d):
    key = '{}_{}'.format(curIndex, left)
    if key in d: return d[key]
    if left <= 0 or curIndex >= len(stack):
        return 0

    if curIndex == len(stack) - 1:
        d[key] = sum(stack[curIndex][-1-left+1:])
        return d[key]

    m = 0
    for i in range(left + 1):
        if i > len(stack[0]):
            break
        if i > 0:
            thisStackSum = sum(stack[curIndex][-1-i+1:])
            m = max(m, thisStackSum + findMax(stack, curIndex + 1, left - i, d))
        else:
            m = max(m, findMax(stack, curIndex + 1, left - i, d))
    d[key] =  m
    return d[key]

for i in range(cases):
    line = input().split()
    N, K, P = int(line[0]), int(line[1]), int(line[2])
    stack = []
    for _ in range(N):
        stack.append([int(item) for item in input().split()][::-1])
    m = findMax(stack, 0, P, dict())
    print('Case #{}: {}'.format(i+1, m))