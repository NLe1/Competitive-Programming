class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = {
            'L': [],
            'R': [],
            '.': []
        }
        l = list(dominoes)
        for cur, ch in enumerate(l):
            d[ch].append(cur)
        if len(d['L']) == 0:
            if len(d['R']) == 0:
                return dominoes
            else:
                return '.' * d['R'][0] + 'R' * (len(dominoes) - d['R'][0])

        if len(d['R']) == 0:
            if len(d['L']) == 0:
                return dominoes
            else:
                return 'L' * (d['L'][-1] + 1) + '.' * (len(dominoes) - d['L'][-1] - 1)

        length = len(d['.'])
        if not length: return dominoes
        ind = 0
        while ind < length:
            cur = d['.'][ind]
            # find the next ends
            end = cur
            while ind + 1 < length and d['.'][ind + 1] == end + 1:
                end += 1
                ind += 1
            if cur == 0:
                if l[end + 1] == 'L':
                    for i in range(cur, end + 1):
                        l[i] = 'L'
            else:
                if end + 1 == len(l):
                    if l[cur-1] == 'R':
                        for i in range(cur, end + 1):
                            l[i] = 'R'
                    break
                if l[end + 1] == 'L' and l[cur - 1] == 'R':
                    a = int((end-cur+1)/2)
                    for i in range(cur, cur+a):
                        l[i] = 'R'
                    for i in range(end, end-a,-1):
                        l[i] = 'L'

                if l[end + 1] == l[cur - 1]:
                    for i in range(cur, end+1):
                        l[i] = 'R' if l[end+1] == 'R' else 'L'
            ind += 1
        return ''.join(l)

s = Solution()
print(s.pushDominoes(".L.R."))
