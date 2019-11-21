class Solution:
    def subarraySum(self, nums, k: int) -> int:
        d,cur,res = {0:1},0,0
        for item in nums:
            cur+=item
            res += d.get(cur-k, 0)
            d[cur]=d.get(cur,0)+1
        return res
