def checkMagazine(magazine, note):
    dict = {}

    for word in magazine:
        if not dict.get(word):
            dict[word] = 1
        else:
            dict[word] += 1

    for word in note:
        if dict.get(word):
            if dict[word] == 1:
                del dict[word]
            else:
                dict[word] -= 1
            continue
        else:
            print("No")
            return

    print("Yes")
    return