digits = [
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1]
    ]
]
chars = []
for x in range(5):
    chars.append(input())

num = []
countNum = int((len(chars[0]) + 1) / 4)
cur = 0
for i in range(countNum):
    thisNum = []
    for j in range(5):
        row = []
        for k in range(cur, cur + 3):
            if chars[j][k] == "*":
                row.append(1)
            else:
                row.append(0)
        thisNum.append(row)
    cur += 4
    num.append(thisNum)

ans = []
dead = False
for item in num:
    if item in digits:
        ans.append(str(digits.index(item)))
    else:
        print("BOOM!!")
        dead = True
        break

if not dead:
    if int(''.join(ans)) % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")