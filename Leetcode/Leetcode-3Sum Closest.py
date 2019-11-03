import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result, diff = 0, sys.maxsize
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                hold_diff = abs (total - target)

                if not hold_diff:
                    return total

                if hold_diff  < diff:
                    result = total
                    diff = hold_diff

                if total < target:
                    left += 1

                else:
                    right -= 1

        return result