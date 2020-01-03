class Solution:
    def rotate(self, nums, k: int) -> None:
        k %= len(nums)
        f,s = nums[len(nums) - k:],nums[:len(nums) - k]
        nums[:len(f)], nums[len(f):] = f,s