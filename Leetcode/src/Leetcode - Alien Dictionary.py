"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

import collections
class Solution:
    def alienOrder(self, words: [str]) -> str:
        map, degree, ans = {}, {}, ""
        for word in words:
            for char in word:
                if char not in map:
                    map[char] = set()
                if char not in degree:
                    degree[char] = 0

        for i in range(len(words) - 1):
            w1,w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j] and w2[j] not in map[w1[j]]:
                    map[w1[j]].add(w2[j])
                    degree[w2[j]]+=1
                    break


        queue = collections.deque()
        for k,v in degree.items():
            if v == 0:
                queue.append(k)
        if len(queue) == len(degree): return ""
        while queue:
            char = queue.popleft()
            ans += char
            for c in map[char]:
                degree[c] -= 1
                if degree[c] == 0:
                    queue.append(c)

        if len(degree) > len(ans)   : return ""
        return ans

s = Solution()
print(s.alienOrder(
["wrt","wrf","er","ett","rftt"]))


