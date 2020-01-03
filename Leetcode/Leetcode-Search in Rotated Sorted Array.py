class Solution:
    def search(self, nums, target: int) -> int:
        # nums = [7,8,9,1,2,3,4]
        start, end = 0, len(nums) - 1
        while start <= end:
            m = start + int((end - start) / 2)
            if nums[m] == target:
                return m

            if target > nums[m]:
                if target >= nums[start] > nums[m]:
                    end = m - 1
                else:
                    start = m + 1
            else:
                if target <= nums[end] < nums[m]:
                    start = m + 1
                else:
                    end = m - 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 8, 1, 2, 3]
               , 8))
