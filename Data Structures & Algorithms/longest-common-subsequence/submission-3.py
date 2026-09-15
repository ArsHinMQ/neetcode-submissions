class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        chars1 = defaultdict(list)
        chars2 = defaultdict(list)
        for i, c in enumerate(text1):
            chars1[c].append(i)
        for i, c in enumerate(text2):
            chars2[c].append(i)

        dp = {}
        def backtrack(i: int = 0, j: int = 0):
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp.get((i, j)):
                return dp[(i, j)]
            c1, c2 = text1[i], text2[j]
            if c1 == c2:
                dp[(i, j)] = 1 + backtrack(i+1, j+1)
                return dp[(i, j)]
            r1, r2 = 0, 0
            if chars2[c1]:
                for nj in chars2[c1]:
                    if nj < j:
                        continue
                    r1 = backtrack(i, nj)
                    break
            if chars1[c2]:
                for ni in chars1[c2]:
                    if ni < i:
                        continue
                    r2 = backtrack(ni, j)
                    break

            dp[(i, j)]= max(r1, r2, backtrack(i+1, j+1))
            return dp[(i, j)]
        return backtrack()
        