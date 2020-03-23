
def computePuddle(elevations, index):
    # started with the current peak
    maxLeft, maxRight = elevations[index], elevations[index]
    # go left
    for i in range(index - 1, -1, -1):
        # account for the maximum possible to to left
        maxLeft = max(maxLeft, elevations[i])

    # go right
    for i in range(index + 1, len(elevations)):
        # account for the maximum possible to to right
        maxRight = max(maxRight, elevations[i])

    # if either left peaks or right peaks is equal to the original height
    # then it can not form a puddle
    if maxLeft == elevations[index] or maxRight == elevations[index]:
        return 0
    else:
        lowerPeak = min(maxLeft, maxRight)
        puddleHeightOnTop = lowerPeak - elevations[index]
        return puddleHeightOnTop



def totalCapturedWater(elevations):
    total = 0
    for i in range(1, len(elevations) - 1):
        total += computePuddle(elevations, i)
    return total

elevations = [6, 3, 6, 2, 7, 4, 5, 3, 8, 1, 3]
print(totalCapturedWater(elevations))