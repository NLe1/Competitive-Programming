import time
class Solution:
    """
        Sub problem if there is only one denominations and the it is not divisible to the amount,
        return -1, else return amount / denomination

        For each denominations, coinChange(coins, deno) == 1, for each deno equal the amount of each
        denomination



    """
    def coinChange(self,  coins, amount) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[-1],-1][dp[-1] == MAX]

start = time.time()
s= Solution()
print(s.coinChange([429,171,485,26,381,31,290]
,8440))

print(time.time() -start)