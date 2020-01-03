import json


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, begin, end, nums):
        print(begin, end)
        if begin == end:
            return TreeNode(nums[begin])
        mid = begin + int((end-begin)/2)
        root = TreeNode(nums[mid])
        if begin != mid:
            root.left = self.helper(begin, mid, nums)
        if mid + 1 != end:
            root.right = self.helper(mid + 1, end, nums)
        return root

    def sortedArrayToBST(self, nums):
        root = self.helper(0, len(nums), nums)
        print(root)


def stringToIntegerList(input):
    return json.loads(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


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
            nums = stringToIntegerList(line);

            ret = Solution().sortedArrayToBST(nums)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
