class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2: return 0
        if prices == sorted(prices, reverse=True): return 0
        l, r = 0, 0
        if length % 2 == 0:
            l = int(length / 2) - 1
            r = int(length / 2)
        else:
            l = r = int(length / 2)

        low = prices[l]
        high = prices[r]
        nl = l if (low <= high) else r
        nh = r if (low <= high) else l
        l -= 1
        r += 1
        m = high - low

        while l >= 0 and r <= length - 1:
            if prices[l] < low: low = prices[l]
            if prices[r] > high: high = prices[r]
            if prices[l] > high and prices[l] > prices[nh]:
                nh = l
            else:
                if prices[nh] - prices[l] > m:
                    m = prices[nh] - prices[l]
                if high - prices[l] > m:
                    m = high - prices[l]
            if prices[r] < low and prices[r] < prices[nl]:
                nl = r
            else:
                if prices[r] - prices[nl] > m:
                    m = prices[r] - prices[nl]
                if prices[r] - low > m:
                    m = prices[r] - low
            l -= 1
            r += 1

        for i in range(0, nh):
            if prices[nh] - prices[i] > m: m = prices[nh] - prices[i]

        for i in range(nl + 1, length):
            if prices[i] - prices[nl] > m: m = prices[i] - prices[nl]
        if m <= 0:
            return 0
        else:
            return m