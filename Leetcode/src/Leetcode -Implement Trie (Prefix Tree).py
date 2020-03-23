class TrieNode:
    def __init__(self, character = '*'):
        self.c = character
        self.children = [None] * 26
        self.isWord = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def getCharIndex(self, character):
        return ord(character) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for ch in word:
            curIndex = self.getCharIndex(ch)
            #if has the character
            if cur.children[curIndex] == None:
                cur.children[curIndex] = TrieNode(ch)
            cur = cur.children[curIndex]
        cur.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for ch in word:
            curIndex = self.getCharIndex(ch)
            if cur.children[curIndex] == None:
                return False
            else:
                cur = cur.children[curIndex]
        if cur.isWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for ch in prefix:
            curIndex = self.getCharIndex(ch)
            if cur.children[curIndex] == None:
                return False
            cur = cur.children[curIndex]
        return True