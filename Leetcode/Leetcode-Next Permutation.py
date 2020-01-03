import bisect


class Solution:
    def nextPermutation(self, nums) -> None:
        if sorted(nums, reverse=True) == nums:
            nums[:] = nums[::-1]
        else:
            i = len(nums) - 2
            while i >= 1:
                if nums[i:] == sorted(nums[i:], reverse=True):
                    i -= 1
                    continue
                else:
                    break
            area = nums[i + 1:]
            area.sort()
            nextNum = area[bisect.bisect_right(area, nums[i])]
            nInd = nums.index(nextNum, i + 1)
            nums[i], nums[nInd] = nums[nInd], nums[i]
            nums[i + 1:] = sorted(nums[i + 1:])


s = Solution()
nums = [2, 3, 1]
s.nextPermutation(nums)
print(nums)
