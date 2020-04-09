"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
import bisect
class Solution:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        construct = []
        res = 0

        for start, end in intervals:
            construct.append((start, True))
            construct.append((end, False))

        construct.sort()

        count = 0

        for i, is_start in construct:
            if is_start:
                count += 1
            else:
                count -= 1

            res = max(res, count)

        return res
s = Solution()
print(s.minMeetingRooms(
    [[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]]
))