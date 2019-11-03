class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ct = 0
        for c in S:
            if c in J: ct += 1

        return ct