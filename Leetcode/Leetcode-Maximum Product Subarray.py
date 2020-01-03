
class Solution:

    def normalize(self ,nums):
        inRun = False
        negative = False
        rec= []
        start = 0,0
        for i,num in enumerate(nums):
            if abs(num) == 1:
                if not inRun:
                    inRun = True
                    start = i
                    negative = not negative if num == -1 else negative
                else:
                    negative = not negative if num == -1 else negative
            else:
                if inRun:
                    rec.append((start, i, negative))
                    negative = False
                    inRun = False
        if inRun:
            rec.append((start, len(nums) + 1,negative))
        for s,e,n in rec:
            nums[s:e] = [-1 if n else 1]
        return nums

    def helper(self, nums):
        if not nums: return 0
        nums = self.normalize(nums)
        product = [item for item in nums]
        for i in range(1, len(product)):
            product[i] *= product[i - 1]

        m = product[0]
        for i in range(1, len(product)):
            m = max([m, nums[i], product[i]])
            for j in range(i):
                m = max(m, product[i] // product[j])
        return m




    def maxProduct(self, nums) -> int:
        index = [i for i in range(len(nums)) if nums[i] == 0]
        start = 0
        m = float('-inf')
        if index:
            for ind in index:
                m = max([self.helper(nums[start:ind]), m, 0])
                start = ind + 1
            m = max([self.helper(nums[start:]), m, 0])
            return m
        else:
            return self.helper(nums)

print(Solution().maxProduct([1,0,-1,2,3,-5,-2]))