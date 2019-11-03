#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    size = len(arr)
    count = 0
    frontI = 0

    while frontI < size:
        if frontI + 1 == arr[frontI]:
            frontI += 1
            continue
        else:
            temp = arr[arr[frontI] - 1]
            arr[arr[frontI] - 1] = arr[frontI]
            arr[frontI] = temp
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()