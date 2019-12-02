class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, ans = float('inf'), float('-inf')
        for item in prices:
            l, ans = min(l, item), max(ans, item - l)
        return max(0, ans)
