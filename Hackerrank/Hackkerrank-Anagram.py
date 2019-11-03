from collections import Counter
def anagram(s):
    length = len(s)
    count = 0
    if length % 2 == 1:
        return -1

    p1 = Counter("".join([x for x in s[int(length/2):]]))
    p2 = Counter("".join([x for x in s[:int(length/2)]]))

    counter = 0
    p = p1 - p2
    for item in p:
       counter += p[item]


    return counter