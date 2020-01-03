def helper(f, t, nums):
    if t == f:
        return 1
    if nums[f:t + 1] == sorted(nums[f:t + 1]):
        return t - f + 1
    mid = f + int((t - f) / 2)
    return max(helper(f, mid, nums), helper(mid + 1, t, nums))


n = int(input())
arr = [int(item) for item in input().strip().split()]
print(helper(0, n - 1, arr))
