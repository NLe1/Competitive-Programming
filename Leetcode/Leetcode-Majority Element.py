class Solution:
    def majorityElement(self, nums) -> int:
        mItem, ct = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == mItem:
                ct+=1
            else:
                if ct == 0:
                    ct = 1
                    mItem = nums[i]
                else:
                    ct -= 1
        return mItem