import bisect
class Solution:
    def checkValidString(self, s: str) -> bool:
        o, st, c = [], [], []
        for ind, ch in enumerate(list(s)):
            if ch == '*':
                st.append(ind)
            elif ch == '(':
                o.append(ind)
            else:
                if len(o) > 0:
                    o.pop()
                else:
                    c.append(ind)

        if len(o) + len(c) == 0:
            return True
        else:
            #excess opening and closing
            for i in range(len(o)-1,-1,-1):
                ind =bisect.bisect(st, o[i])
                if ind == len(st):
                    return False
                else:
                    st.pop(ind)
            for i in range(len(c)):
                ind = bisect.bisect(st, c[i])
                if ind == 0:
                    return False
                else:
                    st.pop(ind-1)
        return True
s=Solution()
print(s.checkValidString("()()((*()()(*()((())()))))(()())))(((()*())))))(())()))((*(())))))()))))())*(())()(()(*))*(*"))