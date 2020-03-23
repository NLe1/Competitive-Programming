class Solution:
    def robSub(self, nums, chooseFirst, index, d):
        key = '{}_{}'.format(index,chooseFirst)
        if index >= len(nums): return 0
        if key in d: return d[key]

        if index == len(nums) - 1:
            if chooseFirst:
                d[key] = 0
                return d[key]
            else:
                d[key] = nums[index]
                return d[key]
        else:
            m = max(self.robSub(nums, chooseFirst, index + 1,d ), nums[index] + self.robSub(nums, chooseFirst, index + 2,d ))
            d[key] = m
            return d[key]

    def rob(self, nums):
        d = dict()
        return max(nums[0] + self.robSub(nums, True, 2, d), self.robSub(nums, False, 1, d))

print(Solution().rob([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]))