"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it i
"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(":")
        unique_digits = set(list(hour) + list(minute))
        if len(unique_digits) == 1: return time
        hour, minute = int(hour), int(minute)
        while True:
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
            hour %= 24
            strHour = str(hour)
            if len(strHour) == 1: strHour = "0" + strHour
            strMinute = str(minute)
            if len(strMinute) == 1: strMinute = "0" + strMinute
            uniq = set(strHour + strMinute)
            if uniq.issubset(unique_digits) or uniq == unique_digits:
                return str(hour) + ":" + str(minute)
s = Solution()
print(s.nextClosestTime("23:59"))


