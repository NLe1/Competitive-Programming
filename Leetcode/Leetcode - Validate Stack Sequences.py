"""
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""

class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        if not pushed: return True
        curPush, curPop = 0, 0
        stack = []
        while curPush < len(pushed):
            if pushed[curPush] != popped[curPop]:
                if stack and popped[curPop] == stack[-1]:
                    stack.pop()
                    curPop += 1
                    continue
                stack.append(pushed[curPush])
                curPush += 1
            else:
                curPop += 1
                curPush += 1
        return stack == popped[curPop:][::-1]
s = Solution()
print(s.validateStackSequences([2,1,0],[1,2,0]))