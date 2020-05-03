#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    # Write your code here
    count = 0
    for ch in s[:k]:
        if ch in "aieou":
            count += 1

    m, ind = count, 0
    for i in range(1, len(s) - k + 1):
        if s[i - 1] in "aieou": count -= 1
        if s[i + k - 1] in "aieou": count += 1
        if count > m:
            m = count
            ind = i
    return s[ind:ind + k]


if __name__ == '__main__':

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    print(result)