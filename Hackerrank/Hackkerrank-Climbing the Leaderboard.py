# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    length = len(scores)
    scores.sort(reverse=True)
    i = 0
    table = {}
    res = []
    sortedAlice = [x for x in alice]
    sortedAlice.sort(reverse=True)

    for j in range(len(sortedAlice)):
        while i < length:
            if i == length - 1 and sortedAlice[j] < scores[i]:
                table[sortedAlice[j]] = i + 2
                break
            if sortedAlice[j] >= scores[i]:
                table[sortedAlice[j]] = i + 1
                break
            i += 1
    for place in alice:
        res.append(table[place])

    return res