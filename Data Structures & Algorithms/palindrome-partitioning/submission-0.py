class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def dfs(i: int = 0):
            nonlocal s
            if i >= len(s):
                res.append(subset.copy())
                return

            base = ""
            for j in range(i, len(s)):
                base += s[j]
                if base != base[::-1]:
                    continue
                subset.append(base)
                dfs(j+1)
                subset.pop()

        dfs()
        return res

        