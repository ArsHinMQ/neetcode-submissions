class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        available_sqaures = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        rows = [{str(num): False for num in range(1, 10)} for _ in range(10)]
        cols = [{str(num): False for num in range(1, 10)} for _ in range(10)]
        squares = {s: {str(num): False for num in range(1, 10)} for s in available_sqaures}

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == ".":
                    continue

                if rows[i][cell]:
                    return False
                rows[i][cell] = True
                
                if cols[j][cell]:
                    return False
                cols[j][cell] = True

                r = i // 3
                c = j // 3
                if squares[(r, c)][cell]:
                    return False
                squares[(r, c)][cell] = True
                        


        return True

        