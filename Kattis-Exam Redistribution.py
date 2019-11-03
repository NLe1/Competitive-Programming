n = int(input())
nums = input().rstrip().split()
nums = [int(x) for x in nums]
srt = sorted(nums, reverse=True)

n = srt[0]
ans = []
for i in range(1,len(srt)):
    n -= srt[i]
if n > 0:
    print("impossible")
else:
    prev = 0
    for i in range(len(srt)):
        if 0 < i < len(srt) and srt[i] == srt[i-1]:
            for j in range(prev + 1, len(srt)):
                if nums[j] == nums[prev]:
                    ans.append(j + 1)
                    prev = j
                    break
        else:
            ind = nums.index(srt[i])
            ans.append(ind + 1)
            prev = ind
    for item in ans:
        print(item, end=" ")