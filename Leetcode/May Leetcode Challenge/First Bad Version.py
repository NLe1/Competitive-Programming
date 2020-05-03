"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        if n == 1: return 1 if isBadVersion(1) else -1
        def helper(low, high):
            nonlocal n
            if abs(high - low) <= 1:
                if isBadVersion(low): return low
                elif isBadVersion(high): return high
                else: return high + 1 if high + 1 <= n else -1
            else:
                middle = low + int((high - low) / 2)
                if isBadVersion(middle):
                    if not isBadVersion(middle - 1): return middle
                    return helper(low, middle - 1)
                else:
                    if isBadVersion(middle + 1): return middle + 1
                    return helper(middle + 1, high)
        return helper(1,n)

