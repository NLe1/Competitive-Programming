from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        ans = []
        for v in cpdomains:
            v = v.split()
            nv = int(v[0])  # number of visits
            v = v[1].split('.')
            for x in range(len(v)):
                d['.'.join(v)] += nv
                v.pop(0)

        for (c, v) in d.items():
            ans.append(str(v) + " " + c)

        return ans