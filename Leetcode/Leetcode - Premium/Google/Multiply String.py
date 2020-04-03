"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                n1 = ord(num1[i]) - ord('0')
                n2 = ord(num2[j]) - ord('0')
                digits[i + j + 1] += n1 * n2
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = int(digits[i]/10)
            digits[i] = (digits[i]) % 10
        ans = []
        cur = 0
        while digits[cur] == 0 and cur <= len(digits) - 2:
            cur+=1
        while cur <= len(digits) - 1:
            ans.append(str(digits[cur]))
            cur+=1
        return ''.join(ans)

s = Solution()
print(s.multiply("0", "0"))