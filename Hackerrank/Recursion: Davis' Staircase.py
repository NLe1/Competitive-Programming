#!/bin/python3

import math
import os
import random
import re
import sys

d = {}

# Complete the stepPerms function below.
def stepPerms(n):
    if n < 1: return 0
    if n in d: return d[n]
    if n == 1 : return 1
    if n == 2 : return 2
    if n == 3: return 4
    res = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    d[n] = res % 10000000007
    return d[n]

if __name__ == '__main__':
    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)
        print(res)