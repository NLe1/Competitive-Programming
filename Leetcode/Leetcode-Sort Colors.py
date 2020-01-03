class Solution:
    def sortColors(self, nums) -> None:
        n = len(nums)
        white, blue = 0, n - 1
        while white <= blue and nums[white] == 0: white += 1
        while blue >= white and nums[blue] == 2: blue -= 1
        if white >= blue: return
        while white < blue:
            if nums[white] > nums[blue]:
                nums[white], nums[blue] = nums[blue], nums[white]
            elif nums[white] == nums[blue]:
                temp = white + 1
                while temp <= blue:
                    if nums[temp] == 2:
                        break
                    if temp == blue:
                        return
                    if nums[temp] == 0:
                        nums[temp], nums[white] = nums[white], nums[temp]
                        white += 1
                    temp += 1
                nums[temp], nums[blue] = nums[blue], nums[temp]
            while white <= blue and nums[white] == 0: white += 1
            while blue >= white and nums[blue] == 2: blue -= 1


s = Solution()
nums = [0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 2, 2, 2, 1]
s.sortColors(nums)
print(nums)
