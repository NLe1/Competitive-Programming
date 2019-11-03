def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    size = len(arr)
    for i in range(size):
        left += arr[i][i]
        right += arr[i][size - i - 1]

    return abs(left - right)