class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        def backtrack(r: int, c: int):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return float("inf")
            elif r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[-1][-1]
            elif (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = grid[r][c] + min(backtrack(r+1, c), backtrack(r, c+1))
            return dp[(r, c)]
        return backtrack(0, 0)
        