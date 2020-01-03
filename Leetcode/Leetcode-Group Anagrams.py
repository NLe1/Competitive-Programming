import collections
class Solution:
    def groupAnagrams(self, strs):
        d = collections.defaultdict(list)
        for word in strs:
            d["".join(sorted(word))].append(word)
        return d.values()

print([1,2,3][1:1])