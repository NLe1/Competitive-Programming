class Solution:
    def jump(self, nums) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times


s = Solution()
print(s.jump([5, 1, 2, 3, 4, 3, 2]))
