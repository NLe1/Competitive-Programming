class Solution:
    def summaryRanges(self, nums):
        if len(nums) <= 1: return len(nums)
        fr, indFr, to, indTo = nums[0],0,nums[0],0
        ans = []
        for i in range(1, len(nums)+1):
            if i < len(nums) and nums[i] - fr == i - indFr:
                to, indTo = nums[i], i
                continue
            else:
                if indFr == indTo:
                    ans.append(str(fr))
                else:
                    ans.append(f"{fr}->{to}")
                if i < len(nums):
                    fr, indFr, to, indTo = nums[i], i, nums[i], i
        return ans


s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))