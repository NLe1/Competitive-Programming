def highestValuePalindrome(s, n, k):
    o = list(s)
    s = list(s)
    if k >= n: return "9" * n
    minStep = 0
    i = 0
    j = n - 1
    # minimum steps
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        if s[i] < s[j]: s[i] = s[j]
        if s[i] > s[j]: s[j] = s[i]
        i += 1
        j -= 1
        minStep += 1

    if minStep > k: return "-1"

    # subtract k from minStep
    k -= minStep
    i = 0

    while k > 0 and i <= n / 2:
        if k == 1 and (s[i] == o[i] and s[n-i-1] == o[n-i-1]) and n % 2 == 1:
            s[int(n/2)] = '9'
            k-=1
            continue

        if s[i] == '9':
            i += 1
            continue
        if s[i] == o[i] and s[n-i-1] == o[n-i-1]:
            k-=2
        else:
            k -= 1
        s[i] = '9'
        s[n - i - 1] = '9'

    return "".join(s)