from heapq import heapify, heappop, heappush

cases = int(input())

for iter in range(cases):
    line = input().rstrip().split()
    size, K = int(line[0]), int(line[1])
    sessions = [int(item) for item in input().split()]
    difficulties = [-1 * (sessions[i] - sessions[i - 1]) for i in range(1, size)]
    heapify(difficulties)

    for _ in range(K):
        if -1 * difficulties[0] == 1:
            break
        top = -1 * heappop(difficulties)
        half = int(top / 2)
        heappush(difficulties, -1 * half)
        heappush(difficulties, -1 * (top - half))

    print('Case #{}: {}'.format(iter + 1, -1 * difficulties[0]))
