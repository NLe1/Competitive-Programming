"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.



Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.
"""


class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        if len(nums) == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]
        def helper(lo, hi):
            nonlocal nums
            cur = lo + int((hi - lo) / 2)
            if nums[cur - 1] != nums[cur] and nums[cur] != nums[cur + 1]: return nums[cur]
            if (cur  % 2 == 0 and nums[cur + 1] == nums[cur]) or (cur % 2 == 1 and nums[cur - 1] == nums[cur]):
                return helper(cur, hi)
            else:
                return helper(lo, cur)
        return helper(0, len(nums) - 1)

s = Solution()
print(s.singleNonDuplicate([3,3,7,7,10,11,11]))