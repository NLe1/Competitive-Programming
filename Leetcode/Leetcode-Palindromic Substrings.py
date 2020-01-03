class Solution:
    def expandAndCount(self, start, end, s):
        if start - 1 < 0 or end + 1 >= len(s) or s[start] != s[end]:
            return 1 if 0 <= start <= end <= len(s) - 1 and s[start] == s[end] else 0
        count, flag, ch = 1, True, s[start]
        while start - 1 >= 0 and end + 1 < len(s):
            if s[start - 1] != s[end + 1]:
                return count
            count += 1
            start -= 1
            end += 1
        return count

    def countSubstrings(self, s: str) -> int:
        # found the cluster
        count, n = 0, len(s)
        for i in range(n):
            count += self.expandAndCount(i, i, s)
            count += self.expandAndCount(i, i + 1, s)
        return count


s = Solution()
print(s.countSubstrings("aabbnmnbgg"))
