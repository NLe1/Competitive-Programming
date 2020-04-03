
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count, n = 0, len(nums)
        cache = {}
        total = 0
        if not nums: return 0
        for i in range(n):
            total += nums[i]
            cache[(0, i)] = total
            if total == k: count += 1
            for j in range(0, i):
                cur = total - cache[(j, i - 1)]
                cache[j + 1, i] = cur
                if cur == k: count += 1
        print(cache)
        return count
s = Solution()
print(s.subarraySum([1,2,1,2,1], 3))



