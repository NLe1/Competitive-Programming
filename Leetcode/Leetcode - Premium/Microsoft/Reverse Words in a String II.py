"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""


class Solution:
    def reverseWords(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        left, right, i = 0, 0, 0
        while right <= len(s) - 1:
            if s[right] != " ":
                right += 1
                continue
            else:
                inLeft, inRight = left, right - 1
                while inLeft < inRight:
                    s[inLeft], s[inRight] = s[inRight], s[inLeft]
                    inLeft += 1
                    inRight -= 1
                left, right = right + 1, right + 1
        right -= 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
arr = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
s = Solution()
print(s.reverseWords(arr))
print(arr)