class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        s = str(num)
        l = len(s)
        it = []
        for i in range(l):
            it.append(s[i] + "0" * (l - i - 1))
        it = [int(a) for a in it]

        for n in it:
            t = None
            if n >= 1000:
                t = int(n / 1000)
                ans += "M" * t
            elif n == 900:
                ans += "CM"
            elif n < 900 and n >= 500:
                ans += "D"
                t = int((n - 500) / 100)
                ans += "C" * t
            elif n == 400:
                ans += "CD"
            elif n < 400 and n >= 100:
                t = int(n / 100)
                ans += "C" * t
            elif n == 90:
                ans += "XC"
            elif n < 90 and n >= 50:
                ans += "L"
                t = int((n - 50) / 10)
                ans += "X" * t
            elif n == 40:
                ans += "XL"
            elif n < 40 and n >= 10:
                t = int(n / 10)
                ans += "X" * t
            elif n == 9:
                ans += "IX"
            elif n < 9 and n >= 5:
                ans += "V"
                t = n - 5
                ans += "I" * t
            elif n == 4:
                ans += "IV"
            else:
                ans += "I" * n
        return ans
