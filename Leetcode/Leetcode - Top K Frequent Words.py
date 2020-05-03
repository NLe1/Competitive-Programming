import collections
class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        c = collections.Counter(words)
        d = list(c.items())
        d.sort(key=lambda x: (- x[1], x[0]))
        return [item for item in d[:k]]

s = Solution()
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))