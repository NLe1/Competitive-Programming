
"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        if len(nums) <= 1: return nums
        ans1 = [1] * len(nums)
        for i in range(1, len(ans1)):
            ans1[i] = ans1[i-1] * nums[i-1]
        ans2 = [1] * len(nums)
        for i in range(len(ans2) - 2, -1, -1):
            ans2[i] = ans2[i+1] * nums[i+1]
        for i in range(len(ans1)):
            ans1[i] *= ans2[i]
        return ans1
s = Solution()
print(s.productExceptSelf([1,2,3,4]))