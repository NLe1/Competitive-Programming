"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

import collections
class Solution:
    def countComponents(self, n: int, edges: [[int]]) -> int:
        seen, ans, neighbors = {}, [], collections.defaultdict(list)
        for node1, node2 in edges:
            neighbors[node1].append(node2)
            neighbors[node2].append(node1)

        for startNode in neighbors:
            if not seen(startNode):
                stack = [startNode]
                connected = []
                while stack:
                    curNode = stack.pop()
                    connected.append(curNode)
                    for neighbor in neighbors[curNode]:
                        if not seen[neighbor]:
                            seen.add(neighbor)
                            stack.append(neighbor)
                ans.append(connected)
        return ans
