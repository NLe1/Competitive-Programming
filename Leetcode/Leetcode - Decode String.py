class Solution:
    def getMultiplier(self, i: int, s: str):
        index = i - 1
        multiplier = []
        while index >= 0:
            if s[index].isnumeric():
                multiplier.append(s[index])
            else:
                break
            index -= 1
        return int(''.join(multiplier[::-1]))

    def decodeString(self, s: str) -> str:
        ans, stack = [], []
        for i, character in enumerate(s):
            # start of pattern
            if character == '[':
                # get the multiplier
                stack.append([self.getMultiplier(i, s)])
                continue
            else:
                if character == ']':
                    innerPattern = stack.pop()
                    multiplier, pattern = innerPattern[0], ''.join(innerPattern[1:])
                    # if stack is empty, add the ans, otherwise add to the top stack
                    if len(stack) == 0:
                        ans.append(multiplier * pattern)
                    else:
                        stack[-1].append(multiplier * pattern)
                elif not character.isnumeric():
                    if len(stack) == 0:
                        ans.append(character)
                    else:
                        stack[-1].append(character)

        assert len(stack) == 0
        return ''.join(ans)

s = Solution()
print(s.decodeString("100[leetcode]"))