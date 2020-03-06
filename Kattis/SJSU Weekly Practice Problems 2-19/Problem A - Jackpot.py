import collections
import math
n = int(input().rstrip())

def product(arr):
    ans = 1
    for number in arr:
        ans *= number
    return ans

def getLCD(arr):
    factorDict = collections.defaultdict(int)
    for number in arr:
        n = number
        factors = collections.defaultdict(int)
        # Print the number of two's that divide n
        while n % 2 == 0:
            factors[2]+=1
            n = int(n / 2)
        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            # while i divides n , print i ad divide n
            while n % i == 0:
                factors[i] += 1
                n = int(n / i)

        # Condition if n is a prime
        # number greater than 2
        if n > 2:
            factors[n] +=1

        for factor, degree in factors.items():
            factorDict[factor] = max(factorDict[factor], degree)
    return product([factor**degree for factor, degree in factorDict.items()])

for _ in range(n):
    numberOfWheels = int(input())
    periodicals = [int(x) for x in input().rstrip().split()]
    ans = getLCD(periodicals)
    if ans > 10**9:
        print("More than a billion.")
    else:
        print(ans)
