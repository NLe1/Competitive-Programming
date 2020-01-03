class Solution:
    def helper(self, nums, target, indexes, start, end):
        if start >= len(nums) or end < 0 or start > end:
            return
        if start == end:
            if nums[start] == target:
                indexes.append(start)
            return
        mid = start + int((end - start) / 2)
        if nums[mid] == target:
            indexes.append(mid)
            self.helper(nums, target, indexes, start, mid - 1)
            self.helper(nums, target, indexes, mid + 1, end)
            return
        elif nums[mid] < target:
            self.helper(nums, target, indexes, mid + 1, end)
        else:
            self.helper(nums, target, indexes, start, mid - 1)
        return

    def searchRange(self, nums, target: int):
        indexes = []
        self.helper(nums, target, indexes, 0, len(nums) - 1)
        indexes.sort()
        if not len(indexes): return [-1, -1]
        return [indexes[0], indexes[-1]]


s = Solution()
print(s.searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))
