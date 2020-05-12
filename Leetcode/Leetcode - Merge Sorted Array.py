"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0: nums1[:n] = nums2
        if n == 0: return
        mainCur, cur1, cur2 = m + n - 1, m - 1, n - 1
        while cur1 >= 0 and cur2 >= 0:
            if nums1[cur1] <= nums2[cur2]:
                nums1[mainCur] = nums2[cur2]
                cur2 -=1
            else:
                nums1[mainCur] = nums1[cur1]
                cur1 -=1
            mainCur -= 1
        while cur2 >= 0:
            nums1[mainCur] = nums2[cur2]
            mainCur-=1
            cur2-=1
        print(nums1)
s = Solution()
print(s.merge([2,0],1,[1],1))