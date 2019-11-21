class Solution:
    def replaceWords(self, dict, sentence: str) -> str:
        dict = sorted(dict, key=len)
        sentence=sentence.split()
        for i,word in enumerate(sentence):
            for root in dict:
                if word.startswith(root):
                    sentence[i] = root
                    break
        return ' '.join(sentence)

s=Solution()
print(s.replaceWords(["dsfsd","cat", "bat", "rat",],"the cattle was rattled by the battery"))