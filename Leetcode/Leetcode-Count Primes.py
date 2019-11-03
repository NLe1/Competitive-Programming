class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        prime = []
        notPrime = set()
        for i in range(2, n):
            if i not in notPrime:
                prime.append(i)
                cur = i + i
                while cur < n:
                    notPrime.add(cur)
                    cur += i

        # print(prime)
        return len(prime)