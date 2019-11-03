#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    b = [False] * 4

    for i in range(len(password)):
        c = password[i] + ""
        if c in numbers:
            b[0] = True

        if c in lower_case:
            b[1] = True

        if c in upper_case:
            b[2] = True

        if c in special_characters:
            b[3] = True

    needed = 0
    for item in b:
        if not item:
            needed += 1

    length = len(password)

    if length < 6:
        if length + needed < 6:
            return 6 - length
        else:
            return needed
    else:
        return needed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()