class Solution:
    def plusOne(self, digits) :
        d = [str(di) for di in digits]
        c = str(int(''.join(d)) + 1)
        return [int(ch) for ch in c]