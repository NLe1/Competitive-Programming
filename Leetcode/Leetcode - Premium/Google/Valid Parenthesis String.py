"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""


class Solution:
    def checkValidString(self, instr: str) -> bool:
        oStack, sStack, cStack = [],[],[]
        for i,ch in enumerate(instr):
            if ch == '*': sStack.append(i)
            elif ch == '(': oStack.append(i)
            else:
                if oStack and oStack[-1] < i:
                    oStack.pop()
                else:
                    cStack.append(i)

        cStack = cStack[::-1]
        sStack = sStack[::-1]
        while cStack:
            if not sStack: break
            if sStack[-1] < cStack[-1]:
                sStack.pop()
                cStack.pop()
            else:
                break

        sStack = sStack[::-1]
        while oStack:
            if not sStack: break
            if sStack[-1] > oStack[-1]:
                sStack.pop()
                oStack.pop()
            else:
                break
        return not (oStack or cStack)

s = Solution()
print(s.checkValidString("((*)*"))
