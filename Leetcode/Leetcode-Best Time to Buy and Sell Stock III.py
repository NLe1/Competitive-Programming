class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2: return 0
        l, h, profits = prices[0], prices[0], []
        for item in prices:
            if item < h:
                if l < h:
                    profits.append((l,h))
                l, h = item, item
            h = max(item, h)
        profits.append((l,h))
        print(profits)
        if len(profits) > 1:
            return profits[-1] + profits[-2]
        else:
            if len(profits) == 1:
                return profits[0]
            else:
                return 0


s = Solution()
print(s.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
