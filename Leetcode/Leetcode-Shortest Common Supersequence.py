class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        dp = [[""] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + text1[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) >= len(dp[i][j - 1]) else dp[i][j - 1]

        for r in dp:
            print(r)
        res, i, j = [], 0, 0
        for c in dp[-1][-1]:
            while text1[i] != c:
                res.append(text1[i])
                i += 1
            while text2[j] != c:
                res.append(text2[j])
                j += 1
            res += c
            i += 1
            j += 1
        res.extend(list(text1[i:]))
        res.extend(list(text2[j:]))
        return "".join(res)


s = Solution()
print(s.shortestCommonSupersequence("abac", "cab"))
