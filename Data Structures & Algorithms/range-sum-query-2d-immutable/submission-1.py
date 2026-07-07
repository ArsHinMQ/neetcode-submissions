class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_length = len(matrix[0])
        col_length = len(matrix)
        prefix_sum_matrix = [[0] * (len(matrix[0]) + 1) for _ in range((len(matrix) + 1))]

        for i in range(1, len(prefix_sum_matrix)):
            row_prefix = prefix_sum_matrix[i]
            for j in range(1, len(prefix_sum_matrix[0])):
                row_prefix[j] = row_prefix[j-1] + prefix_sum_matrix[i-1][j] + matrix[i-1][j-1]
                row_prefix[j] -= prefix_sum_matrix[i-1][j-1]

        self.prefix_sum = prefix_sum_matrix
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1

        total = self.prefix_sum[row2][col2]
        total -= self.prefix_sum[row1-1][col2]
        total -= self.prefix_sum[row2][col1-1]
        total += self.prefix_sum[row1-1][col1-1]
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)