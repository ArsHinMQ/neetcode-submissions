class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        included = set()
        def dfs(r: int = 0, c: int = 0, i: int = 0):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False
            if len(word) == i:
                return True

            cell = board[r][c]
            if cell != word[i]:
                return False
            elif len(word) - 1 == i:
                return True

            options = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            for op in options:
                row, col = op
                key = f"{row}:{col}"
                if key in included:
                    continue
                included.add(key)
                if dfs(row, col, i+1):
                    return True
                included.remove(key)
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                key = f"{r}:{c}"
                included.add(key)
                if dfs(r, c):
                    return True
                included.remove(key)
        return False