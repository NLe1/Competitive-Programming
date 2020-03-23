class Solution:
    def countBits(self, num: int):
        curDegree, index = 0, 0
        ans = [0]
        while True:
            upperLimit = 2 ** curDegree + len(ans) - 1
            if upperLimit <= num:
                for i in range(0, 2**curDegree):
                    ans.append(1 + ans[i])
            else:
                for i in range(0, num - 2**curDegree + 1):
                    ans.append(1 + ans[i])
                break
            curDegree+=1
        return ans
s = Solution()
print(s.countBits(8))