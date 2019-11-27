from collections import Counter
class Solution:
    def dfs(self, nums, sums, index, target):
        if index == len(nums):
            if sums[0] == target and sums[1] == target and sums[2] == target:
                return True
            else:
                return False
        for i in range(4):
            if sums[i] + nums[index] > target: continue
            sums[i] += nums[index]
            if (self.dfs(nums, sums, index + 1, target)): return True
            sums[i] -= nums[index]
        return False

    def makesquare(self, nums) -> bool:
        s = []
        if sum(nums) % 4: return False
        t = int(sum(nums) / 4)
        nums.sort(reverse=True)
        if self.dfs(nums, [0] * 4, 0, t): return True
        return False

s = Solution()
print(s.makesquare([3,3,3,3,4]))
