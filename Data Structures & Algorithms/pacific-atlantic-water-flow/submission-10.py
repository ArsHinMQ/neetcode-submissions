class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        to_atlantic = set()
        to_pacific = set()
        for i in range(rows):
            to_atlantic.add((i, 0))
            to_pacific.add((i, cols-1))
        for i in range(cols):
            to_atlantic.add((0, i))
            to_pacific.add((rows-1, i))

        def bfs(ocean: Set[Tuple[int, int]]):
            queue = deque(list(ocean))
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    elif (nr, nc) in ocean:
                        continue
                    elif heights[nr][nc] < heights[r][c]:
                        continue
                    ocean.add((nr, nc))
                    queue.append((nr, nc))

        bfs(to_atlantic)
        bfs(to_pacific)

        results = []
        for cord in to_atlantic:
            if cord not in to_pacific:
                continue
            results.append(list(cord))

        return results
        
