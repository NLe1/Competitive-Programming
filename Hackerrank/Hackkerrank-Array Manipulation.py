#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    m = 0
    x = 0

    for query in queries:
        arr[query[0]] += query[2]
        if query[1] + 1 <= n:
            arr[query[1] + 1] -= query[2]

    for i in range(1, n + 1):
        x += arr[i]
        m = (x > m) and x or m

    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()