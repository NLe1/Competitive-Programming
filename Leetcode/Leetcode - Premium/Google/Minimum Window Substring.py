"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
   Hide Hint #1
Use two pointers to create a window of letters in S, which would have all the characters from T.
   Hide Hint #2
Since you have to find the minimum window in S which has all the characters from T, you need to expand and contract the window using the two pointers and keep checking the window for all the characters. This approach is also called Sliding Window Approach.

L ------------------------ R , Suppose this is the window that contains all characters of T

        L----------------- R , this is the contracted window. We found a smaller window that still contains all the characters in T

When the window is no longer valid, start expanding again using the right pointer.

"""
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #store the frequency of all unique characters in t
        count_t = collections.Counter(t)
        #store number of unique character in t
        count_unique_t = len(count_t)
        left, right = 0, 0

        #current frequency of the window
        count_window = collections.Counter()
        #keep track of number of unique characters that included in the window
        count_window_unique = 0

        ans = float('inf'), None, None
        while right < len(s):
            char = s[right]
            count_window[char] = count_window.get(char, 0) + 1
            if char in count_t and count_t[char] == count_window[char]:
                count_window_unique += 1

            while left <= right and count_window_unique == count_unique_t:
                character = s[left]

                # Save the smallest window until now.
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                count_window[character] -= 1
                if character in count_t and count_window[character] < count_t[character]:
                    count_window_unique -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                left += 1

            right += 1
        if ans[0] == float("inf"): return ""
        else: return s[ans[1]: ans[2]+ 1]

s =Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))



