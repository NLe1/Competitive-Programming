from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, en) -> int:
        en.sort(key=lambda x: (x[0], -x[1]))
        print(en)
        nums, lis = [j for _, j in en], []
        print(nums)
        for current in nums:
            idx = bisect_left(lis, current)
            lis[idx:idx + 1] = [current]
        print(lis)
        return len(lis)


s = Solution()
print(s.maxEnvelopes([[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]]))