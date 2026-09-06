class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        visited = set()
        for r in range(len(board)):
            if board[r][0] == "O":
                queue.append((r, 0))
                visited.add((r, 0))
            if board[r][len(board[0]) - 1] == "O":
                queue.append((r, len(board[0]) - 1))
                visited.add((r, len(board[0]) - 1))

        for c in range(len(board[0])):
            if board[0][c] == "O":
                queue.append((0, c))
                visited.add((0, c))
            if board[len(board) - 1][c] == "O":
                queue.append((len(board) - 1, c))
                visited.add((len(board) - 1, c))

        while queue:
            r, c = queue.popleft()
            for op in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dr, dc = op
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                    continue
                if (nr, nc) in visited:
                    continue
                if board[nr][nc] == "X":
                    continue
                queue.append((nr, nc))
                visited.add((nr, nc))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) in visited:
                    continue
                board[r][c] = "X"

                
                


        
        