class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        bboard = []
        for _ in range(n):
            r = ["."] * n
            bboard.append(r)

        def backtrack(i: int, board: List[List[str]]):
            if i >= n:
                result = []
                for r in board:
                    row = ""
                    for c in r:
                        row += c
                    result.append(row)
                results.append(result)
                return

            for j in range(n):
                doable = True
                for z in range(n):
                    if board[z][j] != ".":
                        doable = False
                        break

                a, b = i, j
                while a > 0 and b > 0:
                    a -= 1
                    b -= 1
                while a < n - 1 and b < n - 1:
                    if board[a][b] != ".":
                        doable = False
                        break
                    a += 1
                    b += 1

                a, b = i, j
                while a > 0 and b < n - 1:
                    a -= 1
                    b += 1

                while a < n - 1 and b > 0:
                    if board[a][b] != ".":
                        doable = False
                        break
                    a += 1
                    b -= 1

                if not doable:
                    continue

                nboard = [r.copy() for r in board]
                nboard[i][j] = "Q"
                backtrack(i+1, nboard)

        backtrack(0, bboard)
        return results
                
                

        
        