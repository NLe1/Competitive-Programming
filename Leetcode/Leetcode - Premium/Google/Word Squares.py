"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matt
"""

import collections
class Solution:
    def wordSquares(self, words: [str]) -> [[str]]:
        # hash all the words share the same first character
        def helper(firstWord, *rest):
            d, ans = collections.defaultdict(list), ans
            for word in rest:
                if word != firstWord: d[word[0]].append(word)
            for word in words:
                if len(word) == 1: ans.append([word])
                for i in range(1, len(firstWord)):
                    matchChar = firstWord[i]
                    for 

        ans = []
        for word in words:
            res = helper(word, words)
            if res: ans.append(res)
        return ans

