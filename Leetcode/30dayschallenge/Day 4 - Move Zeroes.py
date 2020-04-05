"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        n, countZ = len(nums), nums.count(0)
        pointer, curIndex= 0, 0
        while pointer < n:
            if nums[pointer] != 0:
                nums[curIndex] = nums[pointer]
                curIndex+=1
            pointer+=1
        for i in range(countZ):
            nums[-1-i] = 0
        return
v = [0,1,0,3,12]
s = Solution()
s.moveZeroes(v)
print(v)