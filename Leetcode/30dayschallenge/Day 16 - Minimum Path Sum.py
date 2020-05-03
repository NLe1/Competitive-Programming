"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        if not grid or not grid[0]: return 0
        if len(grid) == 1: return sum(grid[0])
        if len(grid[0]) == 1: return sum([grid[i][0] for i in range(len(grid))])

        graph = [[0] * len(grid[0]) for _ in range(len(grid))]
        graph[-1][-1] = grid[-1][-1]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    continue
                elif i == len(grid) - 1:
                    graph[i][j] = graph[i][j + 1] + grid[i][j]
                elif j == len(grid[0]) - 1:
                    graph[i][j] = graph[i + 1][j] + grid[i][j]
                else:
                    graph[i][j] = min(graph[i + 1][j], graph[i][j + 1]) + grid[i][j]
        return graph[0][0]


s = Solution()
print(s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))