def twoStrings(s1, s2):
    for char in list(s1):
        if char in s2:
            return "YES"

    return "NO"