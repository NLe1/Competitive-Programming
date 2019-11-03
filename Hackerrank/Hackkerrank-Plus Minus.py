def plusMinus(arr):
    total = len(arr)
    p, n, z = 0, 0, 0

    for x in arr:
        if x > 0:
            p += 1
        elif x < 0:
            n += 1
        else:
            z += 1

    p = float(p / total)
    n = float(n / total)
    z = float(z / total)

    print("%.6f\n%.6f\n%.6f" % (p, n, z))