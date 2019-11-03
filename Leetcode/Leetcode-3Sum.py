from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []

        c = Counter(nums)
        li = sorted(list(c.keys()))
        l = 0
        r = len(li) - 1
        ans = []
        while l <= r and li[l] <= 0:
            while l <= r and li[r] >= 0:
                third = -li[l] - li[r]
                if c[third]:
                    if third == 0 and li[l] == 0 and c[0] >= 3:
                        ans.append([0, 0, 0])
                        break
                    cur = li.index(third)
                    if third != 0 or li[l] != 0:
                        if cur == l and c[third] >= 2:
                            ans.append(sorted([third, li[l], li[r]]))
                        elif cur == r and c[third] >= 2:
                            ans.append(sorted([third, li[l], li[r]]))
                        elif l < cur < r:
                            ans.append(sorted([third, li[l], li[r]]))
                r-=1
            l += 1
            r = len(li) - 1

        return ans