import collections


class Library:
    def __init__(self, ID, bookCount, daysToSignUp, booksPerDay, books):
        self.ID = ID
        self.bookCount = bookCount
        self.daysToSignUp = daysToSignUp
        self.booksPerDay = booksPerDay
        self.books = books


"""
  This is multi-comment line
"""

numberOfBooks, numberOfLibraries, daysForScanning = [int(x) for x in input().rstrip().split()]
scores = [int(x) for x in input().rstrip().split()]
libs = []
ratios, maxRatio, maxRatioIndex = [], float('-inf'), float('-inf')

for i in range(numberOfLibraries):

    bookCount, daysToSignUp, booksPerday = [int(x) for x in input().rstrip().split()]

    # if the time it takes to scan lib more than the total time for scanning
    if daysToSignUp >= daysForScanning:
        continue
    books = {}

    sumScores = 0
    for x in input().rstrip().split():
        books[scores[int(x)]] = scores[int(x)]
        sumScores += scores[int(x)]

    # calculate the ratios
    daysTakeForSignUpAndScan = daysToSignUp + bookCount // booksPerday
    ratios.append(sumScores / daysTakeForSignUpAndScan)
    # if ratios[i] > maxRatio:
    #   maxRatio, maxRatioIndex = ratios[i], maxRatioIndex

    libs.append(Library(i, bookCount, daysToSignUp, booksPerday, books))

maxRatio = max(ratios)
maxRatioIndex = ratios.index(maxRatio)
currentDay = 0
chosen = [False] * numberOfBooks

# while currentDay < daysForScanning:
#     # days needed for sign up
#     currentDay += libs[maxRatioIndex].daysToSignUp
#
#     # for



