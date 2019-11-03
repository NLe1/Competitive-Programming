#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    r = math.floor(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))

    foo = ""

    for i in range(c):
        for j in range(i,len(s),c):
            foo+=s[j]
        foo+=" "
    return foo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()