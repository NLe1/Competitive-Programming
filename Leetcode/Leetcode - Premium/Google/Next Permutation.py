"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


import bisect


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if list(sorted(nums))[::-1] == nums:
            nums.sort()
            return

        digits = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < digits[-1]:
                index = bisect.bisect(digits, nums[i])
                nextDigit = digits[index]
                digits[index] = nums[i]
                digits.sort()
                digits = [nextDigit] + digits
                for j in range(i, len(nums)):
                    nums[j] = digits[j - i]
                return
            else:
                digits.append(nums[i])
        return

s = Solution()
arr = [1,2]
s.nextPermutation(arr)
print(arr)
