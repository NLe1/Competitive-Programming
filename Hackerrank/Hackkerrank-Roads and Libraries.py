from collections import deque
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road: return c_lib * n
    c = n
    m = len(cities)
    map = {}
    for src, dest in cities:
        if not map.get(src):
            map[src] = [dest]
        else:
            map[src].append(dest)
        if not map.get(dest):
            map[dest] = [src]
        else:
            map[dest].append(src)
    cost = 0
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i] and map.get(i):
            visited[i] = 1
            ct = 0
            q = deque()
            q.append(i)
            while len(q) > 0:
                cur = q.popleft()
                ct += 1
                if map[cur]:
                    for connect_cities in map[cur]:
                        if not visited[connect_cities]:
                            q.append(connect_cities)
                            visited[connect_cities] = 1
            cost += (ct - 1) * c_road + c_lib
            c -= ct

    return cost + (c) * c_lib