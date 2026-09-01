class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        characters = {}
        for i, c in enumerate(s):
            if c in characters:
                characters[c] = (characters[c][0], i)
            else:
                characters[c] = (i, i)

        res = []
        l, r = characters[s[0]]
        res = [(r+1)-l]
        prev = s[0]
        visited = set(prev)
        i = r + 1
        for c in s:
            if c in visited:
                continue
            visited.add(c)
            l, r = characters[c]
            pl, pr = characters[prev]
            if pl < l and pr > l:
                if r < pr:
                    # within the prev substring
                    continue
                else:
                    res.pop()
                    res.append((r+1)-pl)
                    prev = c
                    characters[c] = (pl, r)
            else:
                res.append((r+1)-l)
                prev = c
        return res
                

        