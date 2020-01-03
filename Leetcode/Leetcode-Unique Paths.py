class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        map = [[0] * (n) for i in range(m)]
        for i in range(m):
            map[i].append(1)
        map.append([1] * (n + 1))
        for i in range(m - 1, 0, -1):
            for j in range(n - 1, 0, -1):
                map[i][j] = map[i+1][j] + map[i][j+1]
        return map[1][1]
s = Solution()
print(s.uniquePaths(3,7))