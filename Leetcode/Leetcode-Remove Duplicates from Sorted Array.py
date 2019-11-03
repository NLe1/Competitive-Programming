class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        counter = 1
        cur = nums[0]
        length = 1
        for item in nums:
            if item == cur: continue
            if item > cur:
                cur = item
                nums[counter] = item
                length += 1
                counter += 1
        return length
