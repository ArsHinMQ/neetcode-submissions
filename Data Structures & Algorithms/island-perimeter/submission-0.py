class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def bfs(r: int, c: int):
            perimeter = 0
            visited.add((r, c))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue
                elif nr >= len(grid) or nc >= len(grid[0]) or nr < 0 or nc < 0:
                    perimeter += 1
                elif grid[nr][nc] == 0:
                    perimeter += 1
                else:
                    perimeter += bfs(nr, nc)
            return perimeter
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return bfs(r, c)
                
        