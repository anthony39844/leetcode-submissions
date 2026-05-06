class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        if j == 0 and len(matrix) == 1:
            return matrix[0][0] == target

        while i < len(matrix):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
                if j < 0:
                    return False
            elif matrix[i][j] < target:
                i += 1
        return False
        
