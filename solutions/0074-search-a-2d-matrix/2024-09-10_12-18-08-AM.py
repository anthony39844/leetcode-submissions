class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if matrix[i][r] < target:
                continue
            elif matrix[i][r] > target:
                while l < r:
                    mid = (l + r) // 2
                    if matrix[i][mid] < target:
                        l += 1
                    elif matrix[i][mid] > target:
                        r -= 1
                    else:
                        return True
            else:
                return True

        return False
