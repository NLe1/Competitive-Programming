from collections import Counter
class Solution:
    def singleNumber(self, nums) -> int:
        c = Counter(nums)
        for k,v in c.items():
            if v == 1: return k