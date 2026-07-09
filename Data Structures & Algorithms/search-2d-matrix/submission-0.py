class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        row_index = -1
        while l < r:
            m = (l + r) // 2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row_index = m
                break
            elif matrix[m][0] > target:
                r = m
            else:
                l = m + 1
        
        if row_index == -1:
            return False

        row = matrix[row_index]
        l, r = 0, len(row)
        while l < r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m
            else:
                l = m + 1
        
        return False
        