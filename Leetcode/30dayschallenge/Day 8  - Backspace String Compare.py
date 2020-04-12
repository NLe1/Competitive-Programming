"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

import itertools
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            count = 0
            for ch in s[::-1]:
                if count == 0 and ch != "#": yield ch
                if ch == "#": count+=1
                elif count > 0 and ch != "#": count-=1
        print(list(itertools.zip_longest(helper(S), helper(T))))
        ta = [s == t for s, t in itertools.zip_longest(helper(S), helper(T))]
        return all(ta)

s = Solution()
print(s.backspaceCompare("ab#c","ad#c"))