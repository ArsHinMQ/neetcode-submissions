class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_counter += 1
                if grid[r][c] != 2:
                    continue
                queue.append((r, c, 0))
        
        mins = 0
        visited = set()
        while queue:
            r, c, m = queue.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if grid[r][c] == 0:
                continue
            elif grid[r][c] == 1:
                fresh_counter -= 1
            mins = max(m, mins)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and (nr, nc) not in visited:
                    queue.append((nr, nc, m+1))
                    
        return mins if fresh_counter == 0 else -1