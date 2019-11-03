class Solution:
    def minCost(self, cur, max, cost, d):
        if f'{cur}' in d.keys(): return d[f'{cur}']
        if cur > max:
            return 0
        else:
            m = min(self.minCost(cur + 1, max, cost, d) + cost[cur], self.minCost(cur + 2, max, cost, d) + cost[cur])
            d[f'{cur}'] = m
            return m

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = dict()
        return min(self.minCost(0, len(cost) - 1, cost, d), self.minCost(1, len(cost) - 1, cost, d))