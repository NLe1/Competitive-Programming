#!/bin/python3

import os
import collections

# Complete the freqQuery function below.
def freqQuery(queries):
    freq = collections.Counter()

    cnt = collections.Counter()

    arr = []

    for q in queries:
        if q[0] == 1:
            cnt[freq[q[1]]] -= 1
            freq[q[1]] += 1
            cnt[freq[q[1]]] += 1

        elif q[0] == 2:
            if freq[q[1]] > 0:
                cnt[freq[q[1]]] -= 1
                freq[q[1]] -= 1
                cnt[freq[q[1]]] += 1

        else:
            if cnt[q[1]] > 0:
                arr.append(1)
            else:
                arr.append(0)

    return arr


if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)