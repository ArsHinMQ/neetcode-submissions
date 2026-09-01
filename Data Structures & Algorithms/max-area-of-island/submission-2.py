class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r: int, c: int):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return 0
            if (r, c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
            visited.add((r, c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                count = max(count, dfs(i, j))
        
        return count
        