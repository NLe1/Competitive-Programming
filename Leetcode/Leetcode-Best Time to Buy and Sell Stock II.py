class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2: return 0
        l, h, ans = prices[0], prices[0], 0
        for item in prices:
            if item < h:
                if l < h:
                    ans += h - l
                l, h = item, item
            h = max(item, h)
        return ans + h - l


s = Solution()
print(s.maxProfit([1,2,3,4,5,4]))
