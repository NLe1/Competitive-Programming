class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        total = int(n*(n+1)/2)
        return total - sum(nums)

s =Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))