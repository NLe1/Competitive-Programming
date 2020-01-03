from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        ans = []
        for k, v in c1.items():
            ans.extend([k] * min(v, c2.get(k, 0)))
        return ans
s = Solution()
print(s.intersect([4,9,5],[9,4,9,8,4]))