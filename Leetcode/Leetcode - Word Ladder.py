"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        d = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                d[word[:i] + "_" + word[i + 1:]].add(word)

        ans,seen = float('inf'),set()
        q = collections.deque([(beginWord, 1)])
        while q:
            curWord, steps= q.popleft()
            for i in range(len(word)):
                for nextWord in d[curWord[:i] + "_" + curWord[i + 1:]]:
                    if nextWord not in seen:
                        if nextWord == endWord:
                            return steps + 1
                        q.append((nextWord, steps + 1))
                        seen.add(nextWord)
        return ans if ans != float('inf') else 0

s = Solution()
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
