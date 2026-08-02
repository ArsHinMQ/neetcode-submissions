class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        row = None
        while l < r:
            m = (l + r) // 2
            first, last = matrix[m][0], matrix[m][-1]
            if first <= target and last >= target:
                row = matrix[m]
                break
            elif first > target:
                r = m
            else:
                l = m + 1
        
        if row is None:
            return False

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
        