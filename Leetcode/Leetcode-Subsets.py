import collections

class Solution:
    def subsets(self, nums):
        if not nums: return [[]]
        queue, ans, n = collections.deque([([num], i) for i, num in enumerate(nums)]),[[]], len(nums)
        while queue:
            cur, i = queue.popleft()
            ans.append(cur)
            while i != n - 1:
                queue.append((cur + [nums[i+1]], i+1))
                i+=1
        return ans

print(Solution().subsets([34,2,36,72,36,27,5682,313,3,7,0,5,213,4623]))
