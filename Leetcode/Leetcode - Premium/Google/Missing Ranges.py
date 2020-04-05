"""Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""


class Solution:
    def findMissingRanges(self, nums: [int], lower: int, upper: int) -> [str]:
        ans, nums = [], [lower - 1] + nums + [upper + 1]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                ans.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:
                ans.append('{}->{}'.format(nums[i] + 1, nums[i + 1] - 1))
        return ans

s = Solution()
print(s.findMissingRanges([0, 1, 3, 50, 75],0,99))
