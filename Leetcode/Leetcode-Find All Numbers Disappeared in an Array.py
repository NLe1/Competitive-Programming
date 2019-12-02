class Solution:
    def findDisappearedNumbers(self, nums):
        nums.sort()
        ans = []
        cur = 0
        for item in nums:
            if item == cur:
                continue
            else:
                for i in range(cur + 1, item):
                    ans.append(i)
                cur = item
        for i in range(cur + 1, len(nums) + 1):
            ans.append(i)
        return ans
s = Solution()
print(s.findDisappearedNumbers([2,5,5,5,5]))
