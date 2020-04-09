"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        i = 0
        words = ""

        def helper(n):
            if n == 0: return ""
            if n < 20:
                return " " + less_than_20[n]
            if n < 100:
                return tens[int(n/10)] + helper(n % 10)
            else:
                return less_than_20[int(n/100)] + " Hundred " + helper(n % 100)

        while num > 0:
            if num % 1000 > 0:
                words = helper(num % 1000) + " " + thousands[i] + " " + words
            num = int(num/1000)
            i+=1
        return words.strip()

s = Solution()
print(s.numberToWords(1234567891))