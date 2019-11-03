class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        num = 0
        i = 0
        while i < l:
            if s[i] == 'I' and i + 1 < l and s[i + 1] != 'I':
                if s[i + 1] == 'V':
                    num += 4
                    i += 2
                    continue
                elif s[i + 1] == 'X':
                    num += 9
                    i += 2
                    continue
            if s[i] == 'X' and i + 1 < l and s[i + 1] != 'X':
                if s[i + 1] == 'L':
                    num += 40
                    i += 2
                    continue
                elif s[i + 1] == 'C':
                    num += 90
                    i += 2
                    continue
            if s[i] == 'C' and i + 1 < l and s[i + 1] != 'C':
                if s[i + 1] == 'D':
                    num += 400
                    i += 2
                    continue
                elif s[i + 1] == 'M':
                    num += 900
                    i += 2
                    continue
            if s[i] == 'I':
                num += 1
            if s[i] == 'V':
                num += 5
            if s[i] == 'X':
                num += 10
            if s[i] == 'L':
                num += 50
            if s[i] == 'C':
                num += 100
            if s[i] == 'D':
                num += 500
            if s[i] == 'M':
                num += 1000
            i += 1

        return num