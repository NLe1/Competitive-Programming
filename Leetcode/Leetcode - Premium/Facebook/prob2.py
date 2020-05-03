def restoreIpAddresses(s: str) -> [str]:
    def helper(index, s):
        if s == "": return []
        if index == 4: return [s] if 0 <= int(s) <= 255 else []
        ans = []
        if s[0] == '0':
            before = '0'
            ret = helper(index + 1, s[1:])
            for after in ret:
                ans.append(before + '.' + after)
        else:
            for i in range(1, min(4, len(s))):
                if 0 <= int(s[:i]) <= 255:
                    before = s[:i]
                    ret = helper(index + 1, s[i:])
                    for after in ret:
                        ans.append(before + '.' + after)
        return ans

    return helper(1, s)
print(restoreIpAddresses("010010"))