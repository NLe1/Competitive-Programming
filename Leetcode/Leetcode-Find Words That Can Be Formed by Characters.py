from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(list(chars))
        count = 0
        for word in words:
            able = True
            c1 = Counter(list(word))
            for ch,n in c1.items():
                #if not be able to make a word from chars, continue
                if ch not in c or c1[ch] > c[ch]:
                    able = False
                    break
            if able: count += len(word)

        return count