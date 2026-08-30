class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checked = set()
        def dfs(r: int, c: int):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            if (r, c) in checked:
                return
            if grid[r][c] == "0":
                return
            checked.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cell = grid[r][c]
                if cell == "0":
                    continue
                if (r, c) in checked:
                    continue
                dfs(r, c)
                count += 1

        return count
                
        