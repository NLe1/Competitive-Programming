import collections
class Solution:
    def gardenNoAdj(self, N, paths):
        if N ==1:
            return [1]
        d= collections.defaultdict(list)
        for a,b in paths:
            d[a-1].append(b-1)
            d[b-1].append(a-1)
        ans = [-1] * N
        visited = [False] * N
        stack = [0]
        for curGarden, neighborGardens in d.items():
            for connectedGarden in neighborGardens:
                if ans[connectedGarden] == -1:
                    #choose the optimal type of flower based on the flowers of its neighbor
                    neighborFlowers = []
                    for neighbor in d[connectedGarden]:
                        neighborFlowers.append(ans[neighbor])
                        if visited[neighbor]:
                            stack.append(neighbor)
                    for i in range(1,5):
                        if i not in neighborFlowers:
                            ans[connectedGarden] = i
                            break
                    visited[connectedGarden] = True
        return [1 if x == -1 else x for x in ans]
s = Solution()
print(s.gardenNoAdj(10000,[]))

