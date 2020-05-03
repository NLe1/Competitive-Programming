"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums: [int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            m = start + int((end - start) / 2)
            if nums[m] == target:
                return m

            if target > nums[m]:
                if target >= nums[start] > nums[m]:
                    end = m - 1
                else:
                    start = m + 1
            else:
                if target <= nums[end] < nums[m]:
                    start = m + 1
                else:
                    end = m - 1
        return -1

s = Solution()
print(s.search( [5,1,3],3))