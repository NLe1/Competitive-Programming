from collections import Counter
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for x in A:
            if A.count(x) > 1:
                return x