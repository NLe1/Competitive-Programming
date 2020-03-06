class Solution:
    def wordBreak(self, s: str, wordDict, d = None, pos = 0) -> bool:
        w = set(s)
        if not w.issubset(set(''.join(wordDict))):
            return False
        if d == None:
            d = dict()
        if pos in d: return d[pos]
        for word in wordDict:
            if s.startswith(word):
                if s == word or self.wordBreak(s[len(word):], wordDict, d, pos + len(word)):
                    return True
        d[pos] = False
        return False


print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
,["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]))