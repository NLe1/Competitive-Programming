import itertools
class Solution:
    def permute(self, nums):
        return list(list(item) for item in itertools.permutations(nums))

s = Solution()
print(s.permute([1,2,3,4]))