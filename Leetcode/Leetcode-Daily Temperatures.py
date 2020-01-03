class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        if n == 1:
            return T
        ans = [0] * n
        for i in range(n - 2, -1, -1):
            if T[i] < T[i + 1]:
                ans[i] = 1
                continue
            else:
                if ans[i + 1] == 0:
                    ans[i] = 0
                    continue
                nInd = i + 1 + ans[i + 1]
                while T[nInd] <= T[i] and ans[nInd] > 0:
                    nInd += ans[nInd]
                if ans[nInd] == 0:
                    if T[nInd] <= T[i]:
                        ans[i] = 0
                        continue
                    else:
                        ans[i] = nInd - i
                else:
                    ans[i] = nInd - i
        return ans
s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
