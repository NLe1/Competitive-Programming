class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ans = []
        if A == B:
            return "ab" * A
        while A > 0 and B > 0:
            if A > B:
                if A>1 and B>0:
                    ans.append("aab")
                    A-=2
                    B-=1
                else:
                    ans.append("ab")
                    A-=1
                    B-=1
            else:
                if B > 1 and A > 0:
                    ans.append("bba")
                    B-=2
                    A-=1
                else:
                    ans.append("ab")
                    A-=1
                    B-=1
            if A == B:
                break
        if A == B:
            if ans[-1][-1] == 'b':
                ans.append("ab"*A)
            else:
                ans.append("ba"*A)
        else:
            if A:
                ans.append("a"*A)
            else:
                ans.append("b"*B)
        return "".join(ans)
s = Solution()
print(s.strWithout3a3b(3,4))

