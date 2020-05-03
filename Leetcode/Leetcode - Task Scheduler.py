"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

import collections
from heapq import heapify, heappop
class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        ops,c = len(tasks), collections.Counter(tasks)
        counts = [-count for count in c.values()]
        heapify(counts)
        tasks = 0
        while counts:
            nextLCount = -1 * heappop(counts)
            opsLeft = ops - nextLCount
            vacant = (nextLCount - 1) * n
            if counts[0] * -1 == nextLCount
            if vacant >= opsLeft:
                lCount = int(ops / n) + 2
                return tasks + (lCount - 1) * n + lCount
            else:
                tasks += (vacant + nextLCount)
                ops-=nextLCount

s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))