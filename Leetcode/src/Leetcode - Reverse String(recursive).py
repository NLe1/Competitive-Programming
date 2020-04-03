class Solution:
    def reverseString(self, s: List[str], index = 0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if index == len(s) - 1:
            s[0] = s[-1]
            return 1
        else:
            retIndex = self.reverseString(s, index + 1)
            s[retIndex] = s[]


