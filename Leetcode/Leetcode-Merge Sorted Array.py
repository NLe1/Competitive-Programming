import json


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        if len(nums2) == 0:
            return
        cur = len(nums1) - 1
        while cur >= 0:
            if nums1[cur] == 0:
                cur -= 1
            else:
                break
        temp = nums1[:cur + 1] + nums2
        temp.sort()
        for i in range(len(temp)):
            nums1[i] = temp[i]


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            m = int(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);
            line = next(lines)
            n = int(line);

            ret = Solution().merge(nums1, m, nums2, n)

            out = integerListToString(nums1)
            if ret is not None:
                print("Do not return anything, modify nums1 in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
