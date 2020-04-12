#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindrome(s):
    # List of all characters
    chars = list(s)
    # set of seen palindromes
    seen = set()
    def expandAndFind(left, right):
        #the string join from list of characters
        curStr = ''.join(chars[left:right+1])
        if curStr not in seen: seen.add(curStr)

        #expand from middle
        while left - 1 >= 0 and right + 1 <= len(chars) - 1 and chars[left - 1] == chars[right + 1]:
            left-=1
            right+=1
            curStr = ''.join(chars[left:right+1])
            if curStr not in seen: seen.add(curStr)

    for i, ch in enumerate(chars):
        #expand with one middle character
        expandAndFind(i, i)
        #expand with two equal middle characters
        if i + 1 <= len(chars) - 1 and chars[i + 1] == ch:
            expandAndFind(i,i+1)
    print(list(seen))
    return len(seen)

if __name__ == '__main__':
    s = input()

    result = palindrome(s)

    print(str(result) + '\n')