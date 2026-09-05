class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = {}
        queue = deque()

        for i in range(len(heights[0])):
            pacific[(0, i)] = True
            queue.append((0, i))
        for i in range(len(heights)):
            pacific[(i, 0)] = True
            queue.append((i, 0))

        while queue:
            r, c = queue.pop()
            h = heights[r][c]
            for op in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dr, dc = op
                nr, nc = r + dr, c + dc

                if nr >= len(heights) or nc >= len(heights[0]) or nr < 0 or nc < 0:
                    continue
                elif heights[nr][nc] < h:
                    continue
                elif pacific.get((nr, nc)) is not None:
                    continue
                pacific[(nr, nc)] = True
                queue.append((nr, nc))

        atlantic = {}
        queue = deque()
        for i in range(len(heights[0])):
            queue.append((len(heights) - 1, i))
            atlantic[(len(heights) - 1, i)] = True

        for i in range(len(heights)):
            queue.append((i, len(heights[0]) - 1))
            atlantic[(i, len(heights[0]) - 1)] = True

        while queue:
            r, c = queue.pop()
            h = heights[r][c]
            for op in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dr, dc = op
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >= len(heights) or nc >= len(heights[0]):
                    continue
                elif heights[nr][nc] < h:
                    continue
                elif atlantic.get((nr, nc)) is not None:
                    continue
                atlantic[(nr, nc)] = True
                queue.append((nr, nc))
        
        res = []
        print(pacific)
        print(atlantic)
        for item in pacific:
            if atlantic.get(item):
                res.append(list(item))

        return res
        
                
            