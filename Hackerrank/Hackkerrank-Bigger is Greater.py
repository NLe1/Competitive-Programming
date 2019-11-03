def biggerIsGreater(w):
    s = sorted(w, reverse=True)
    length = len(w)
    if w == "".join(s):
        return "no answer"

    for i in range(length - 2, 0, -1):
        has = []
        for j in range(i + 1, length):
            if w[j] > w[i]:
                has.append(w[j])
        if len(has) > 0:
            has.sort()
            temp = w[::-1]
            index = length - temp.index(has[0]) - 1
            l = list(w)
            l[i], l[index] = l[index], l[i]
            w = "".join(l)
            p1 = w[:i+1]
            p2 = w[i+1:]
            return p1+"".join(sorted(p2))

    index = s.index(w[0]) - 1
    while s[index - 1] <= w[0] and index > 0: index -= 1
    c = s.pop(index)
    return c + "".join(sorted(s))