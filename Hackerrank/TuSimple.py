#!/bin/python3
# import math
import os
import random
import re
import sys


#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

def droppedRequests(requestTime):
    startTime, requestCount, timeIndex, numRequest, numDrop = 0, 0, dict(), [], 0
    for i,request in enumerate(requestTime):
        if request != startTime:
            startTime = request
            requestCount = 1
            timeIndex[startTime] = i
        else:
            requestCount+=1
        lastRequestIndex, lastRequestCount = numRequest[-1] if len(numRequest) > 0 else startTime, requestCount

        if len(numRequest) == 0:
            numRequest.append([startTime, requestCount])
            continue

        if requestCount <= 4 and numRequest[timeIndex[startTime]][1] - numRequest[timeIndex.get(max(startTime - 9, 1),0)][1] <= 20 and numRequest[timeIndex[startTime]][1] - numRequest[timeIndex[max(startTime - 59, 1)]][1] <= 60:
            numRequest.append([startTime, lastRequestCount + 1])
            if requestCount == 4:
                numDrop += 1
        else:
            numRequest.append([startTime, lastRequestCount])
            numDrop += 1
    return numDrop



s =  [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]
print(droppedRequests(s))
