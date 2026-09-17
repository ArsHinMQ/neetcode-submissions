class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mem = {}
        def dfs(r: int = 0, c: int = 0, prev: int | float = float("-inf")):
            if r >= len(matrix) or c >= len(matrix[0]) or r < 0 or c < 0:
                return 0
            elif (r, c, prev) not in mem:
                if matrix[r][c] <= prev:
                    mem[(r, c, prev)] = 0
                else:
                    mem[(r, c, prev)] = 1 + max(dfs(r+1, c, matrix[r][c]), dfs(r, c+1, matrix[r][c]), dfs(r-1, c, matrix[r][c]), dfs(r, c-1, matrix[r][c]))
            return mem[(r, c, prev)]

        res = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c))
        return res