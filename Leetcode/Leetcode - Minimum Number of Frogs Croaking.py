"""
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.



Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1


Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
"""
import collections
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = {'c':'r','r':'o','o':'a','a':'k','k':'c'}
        m,cur,next = 0,0, collections.defaultdict(int)
        next['c']+=1
        for ch in croakOfFrogs:
            if next[ch] == 0 and ch != 'c': return -1
            elif ch == 'c': cur+=1
            elif ch == 'k': cur-=1
            m = max(m,cur)
            if ch != 'c' or next[ch] > 1: next[ch] -= 1
            next[d[ch]]+=1
        return m if all([next[ch] == 0 for ch in next.keys() if ch != 'c']) else -1

s = Solution()
print(s.minNumberOfFrogs("croakcroa"))



