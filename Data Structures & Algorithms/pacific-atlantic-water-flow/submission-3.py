class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        po = {}
        ao = {}

        for i in range(len(heights[0])):
            po[(0, i)] = True
            ao[(len(heights) - 1, i)] = True
        for i in range(len(heights)):
            po[(i, 0)] = True
            ao[(i, len(heights[0]) - 1)] = True
        
        res = []
        def dfs_po(r: int, c: int):
            if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                return False
            cord = (r, c)
            if po.get(cord) is not None:
                if po[cord] == "calc":
                    return False
                return po[cord]

            po[cord] = "calc"
            if r-1 >= 0 and heights[r-1][c] <= heights[r][c] and dfs_po(r-1, c):
                po[cord] = True
            if po[cord] == "calc" and r+1 < len(heights) and heights[r+1][c] <= heights[r][c] and dfs_po(r+1, c):
                po[cord] = True
            if po[cord] == "calc" and c-1 >= 0 and heights[r][c-1] <= heights[r][c] and dfs_po(r, c-1):
                po[cord] = True
            if po[cord] == "calc" and c+1 < len(heights[0]) and heights[r][c+1] <= heights[r][c] and dfs_po(r, c+1):
                po[cord] = True
            if po[cord] == "calc":
                po[cord] = False

            return po[cord]

        def dfs_ao(r: int, c: int):
            if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                return False
            cord = (r, c)
            if ao.get(cord) is not None:
                if ao[cord] == "calc":
                    return False
                return ao[cord]

            ao[cord] = "calc"
            if r-1 >= 0 and heights[r-1][c] <= heights[r][c] and dfs_ao(r-1, c):
                ao[cord] = True
            if ao[cord] == "calc" and r+1 < len(heights) and heights[r+1][c] <= heights[r][c] and dfs_ao(r+1, c):
                ao[cord] = True
            if ao[cord] == "calc" and c-1 >= 0 and heights[r][c-1] <= heights[r][c] and dfs_ao(r, c-1):
                ao[cord] = True
            elif ao[cord] == "calc" and c+1 < len(heights[0]) and heights[r][c+1] <= heights[r][c] and dfs_ao(r, c+1):
                ao[cord] = True
            if ao[cord] == "calc":
                ao[cord] = False

            return ao[cord]

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if not dfs_po(r, c):
                    continue
                elif not dfs_ao(r, c):
                    continue
                res.append([r, c])

        return res
        
                
            