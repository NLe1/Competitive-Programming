class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        nS = sorted(nums)
        fr, to = 0, len(nums) - 1
        while fr < to:
            if nums[fr] == nS[fr]:
                fr += 1
            else:
                break
        while fr < to:
            if nums[to] == nS[to]:
                to -= 1
            else:
                break
        return to - fr + 1 if fr < to else 0


s = Solution()
print(s.findUnsortedSubarray([1, 2, 2, 4, 3, 2]))
