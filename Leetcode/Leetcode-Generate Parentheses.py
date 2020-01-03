class Solution:
    def generateParenthesis(self, n: int):
        self.valid_parentheses = []

        def recursion(l, r, s):
            if len(s) == n * 2:
                self.valid_parentheses.append(s)
            if l < n:
                recursion(l + 1, r, s + "(")
            if r < l:
                recursion(l, r + 1, s + ")")

        recursion(0, 0, "")
        return self.valid_parentheses

s = Solution()
print(s.generateParenthesis(5))