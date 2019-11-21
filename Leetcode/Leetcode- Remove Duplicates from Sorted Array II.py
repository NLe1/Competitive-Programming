from collections import Counter
class Solution:
    def removeDuplicates(self, nums) -> int:
        c = Counter(nums)
        i = 0
        for k,v in sorted(c.items()):
            if v >= 2:
                nums[i]=k
                nums[i+1]=k
                i+=2
            else:
                nums[i]=k
                i+=1
        return i

nums = [1,1,1,2,2,3]
s = Solution()
len = s.removeDuplicates(nums);
for i in range(len):
    print(nums[i], end=" ")