class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        start = 0
        ans = []
        cf = text.count(first)
        l = len(text)
        for i in range(cf):
            cur = text.index(first, start)
            if cur + 2 < l and text[cur +1 ] == second:
                ans.append(text[cur+2])
            start = cur + 1
        return ans