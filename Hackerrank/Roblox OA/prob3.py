#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulSubarrays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER numOdds
#

def beautifulSubarrays(arr, numOdds):
    # record every position of odd numbers arr
    pos = [i for i in range(len(arr)) if arr[i] % 2 == 1]
    ans = 0
    # for each batch numOdds at index i to index numOdds + i in pos
    # we have to calculate number of ways that can create a valid array that include arr[i: i + numOdds + 1]
    # if there are two even numbers before index i (until the next previous odd number) and 4 even number after index i + numOdds (until the next after odd number), we'll have (2 + 1) * (4 + 1) ways of creating arrays that includ the base array
    for i in range(len(pos) - numOdds + 1):
        nextPreviousOddIndex = -1 if i == 0 else pos[i - 1]
        nextAfterOddIndex = len(arr) if i + numOdds - 1 == len(pos) - 1 else pos[i + numOdds]

        countLeft = pos[i] - nextPreviousOddIndex - 1
        countRight = nextAfterOddIndex - pos[i + numOdds - 1] - 1
        ans += (countLeft + 1) * (countRight + 1)
    return ans

    # Write your code here


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    numOdds = int(input().strip())

    result = beautifulSubarrays(arr, numOdds)

    print((str(result) + '\n'))