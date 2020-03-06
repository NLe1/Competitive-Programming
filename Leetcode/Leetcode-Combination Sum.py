import collections
class Solution:
    def combinationSum(self, candidates, target: int, d = None):
        candidates.sort()
        if target < candidates[0]: return []
        if not d: d = collections.defaultdict(list)
        if target in d: return d[target]
        newArr = []
        for candidate in candidates:
            if candidate == target:
                newArr.append([candidate])
            if candidate > target:
                break
            res = self.combinationSum(candidates, target - candidate,d)
            if res:
                for ans in res:
                    newArr.append(sorted([candidate] + ans))
        newArr = [list(x) for x in set(tuple(x) for x in newArr)]
        d[target] = newArr
        return newArr

print(Solution().combinationSum([2,3,5],8))