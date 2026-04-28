class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = 0, len(matrix) - 1
        while x <= y:
            mid = (x + y) // 2
            n = len(matrix[mid]) - 1
            if matrix[mid][0] <= target and matrix[mid][n] >= target:
                l, r = 0, n
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            elif matrix[mid][0] < target:
                x = mid + 1
            else: 
                y = mid - 1
        
        return False


