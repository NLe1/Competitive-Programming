class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        openRoom = [False]*len(rooms)
        q = [0]
        openRoom[0] = True
        while len(q) > 0:
            temp = q.pop()
            for key in rooms[temp]:
                if not openRoom[key]:
                    q.append(key)
                    openRoom[key] = True
        if all(openRoom): return True
        return False

s = Solution()
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))