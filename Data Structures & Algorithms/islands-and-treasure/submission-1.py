class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        visited = set()
        
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    continue
                queue.append((r, c, -1))

        while queue:
            r, c, w = queue.popleft()
            if (r, c) in visited:
                continue
            elif grid[r][c] == -1:
                continue
            visited.add((r, c))
            grid[r][c] = w + 1
            if r + 1 < len(grid):
                queue.append((r+1, c, grid[r][c]))
            if r - 1 >= 0:
                queue.append((r-1, c, grid[r][c]))
            if c + 1 < len(grid[0]):
                queue.append((r, c+1, grid[r][c]))
            if c - 1 >= 0:
                queue.append((r, c-1, grid[r][c]))

            