class Solution:
    def helper(self, l, index, curM, curN,d):
        #out of bound
        if index == len(l):
            return 0
        #if memoized
        if (index, curM, curN) in d:
            return d[(index, curM, curN)]
        #if can not afford current index, skip to next one
        if curM < l[index][0] or curN < l[index][1]:
            d[(index, curM, curN)] = self.helper(l, index + 1, curM, curN, d)
            return d[(index, curM, curN)]
        d[(index, curM, curN)] = max(self.helper(l, index + 1, curM, curN, d), 1 + self.helper(l,index+1,curM-l[index][0],curN-l[index][1],d))
        return d[(index, curM, curN)]

    def findMaxForm(self, strs, m: int, n: int) -> int:
        if len(strs) == 0: return 0
        l = [list(s) for s in strs]
        l = [(li.count('0'), li.count('1')) for li in l]
        if len(strs) == 1:
            if m >=  strs[0][0] and n >= strs[0][1]:
                return True
            else:
                return False
        l.sort(key=lambda x: (x[0],x[1]))
        d = {}
        m = max(self.helper(l,0,m,n,d), self.helper(l,1,m-l[0][0],n-l[0][1],d))
        print(d)
        return m

s = Solution()
print(s.findMaxForm(["10", "0", "1"], 1,1))