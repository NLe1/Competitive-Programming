class Solution:
    def helper(self,nums,i):
        if int(nums[i+1]+nums[i]) > int(nums[i]+nums[i+1]):
            nums[i], nums[i+1] = nums[i+1],nums[i]
    def largestNumber(self, nums) -> str:
        r = ''.join(sorted(map(str, nums), lambda x, y: [1, -1][x + y > y + x]))
        print(r)
        return r
s = Solution()
print(s.largestNumber([121,12]))