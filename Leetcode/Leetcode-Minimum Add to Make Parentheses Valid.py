class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        o, c = [],[]
        for i, item in enumerate(list(S)):
            if item == '(':
                o.append(i)
            else:
                if not len(o):
                    c.append(i)
                else:
                    o.pop()
        return len(o) + len(c)

s =Solution()
print(s.minAddToMakeValid("()))(("))