class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_heap = [(0, 0, 0)]
        visited = set()
        while min_heap:
            diff, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return diff

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= len(heights) or nc >= len(heights[0]):
                    continue
                ndiff = abs(heights[r][c] - heights[nr][nc])
                heapq.heappush(min_heap, (max(diff, ndiff), nr, nc))
            

