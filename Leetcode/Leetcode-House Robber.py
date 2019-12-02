class Solution:
    def helper(self, curInd, nums, d):
        if curInd in d: return d[curInd]
        if curInd > len(nums) - 1:
            return 0
        m = nums[curInd] + max(self.helper(curInd + 2, nums, d), self.helper(curInd + 3, nums, d))
        d[curInd] = m
        return m

    def rob(self, nums) -> int:
        d = {}
        return max(self.helper(0, nums, d), self.helper(1, nums, d))

s = Solution()
print(s.rob([1,2,3,1]))
