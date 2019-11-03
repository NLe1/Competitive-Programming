#!/bin/python3
import math
import os
import random
import re
import sys
import copy

# Complete the minimumBribes function below.
def minimumBribes(q):
    size = len(q);
    for i in range(len(q)):
        if q[i] - i - 1 > 2:
            print("Too chaotic")
            return

    c = [i for i in range(1, len(q) + 1)]
    count = 0

    for i in range(len(c)):
        # if in right position, then continue
        if c[i] == q[i]:
            continue

        if i + 1 <= size - 1 and c[i + 1] == q[i]:
            count += 1
            temp = c[i + 1]
            c[i + 1] = c[i]
            c[i] = temp

        if i + 2 <= size - 1 and c[i + 2] == q[i]:
            count += 2
            temp = c[i + 2]
            c[i + 2] = c[i + 1]
            c[i + 1] = c[i]
            c[i] = temp

    print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)