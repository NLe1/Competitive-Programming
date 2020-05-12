"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cR, cM = collections.Counter(ransomNote, magazine)
        for needC, needCount in cR.items():
            if needC not in cM or needCount > cM[needC]: return false
        return True