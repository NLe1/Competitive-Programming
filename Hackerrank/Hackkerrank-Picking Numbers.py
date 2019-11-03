def pickingNumbers(a):
    # Write your code here
    a.sort()

    max = 1
    count = 1
    prev = a[0]

    for i in range(1, len(a)):
        if a[i] == prev or (a[i] - prev) == 1:
            count += 1
        else:
            max = (count > max) and count or max
            count = 1
            prev = a[i]

    if count > max: max = count

    return max