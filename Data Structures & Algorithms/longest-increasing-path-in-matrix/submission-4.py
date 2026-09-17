class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mem = {}
        def dfs(r: int = 0, c: int = 0):
            if (r, c) in mem:
                return mem[(r, c)]

            best = 1
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = r + dr, c + dc
                if nr >= len(matrix) or nr < 0 or nc >= len(matrix[0]) or nc < 0:
                    continue
                elif matrix[nr][nc] <= matrix[r][c]:
                    continue
                best = max(best, 1+dfs(nr, nc))
            mem[(r, c)] = best
            return best

        res = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c))
        return res