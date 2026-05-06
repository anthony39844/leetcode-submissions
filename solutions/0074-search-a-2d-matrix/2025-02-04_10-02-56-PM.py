class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target <= matrix[mid][len(matrix[0]) - 1] and target >= matrix[mid][0]:
                break
            elif target > matrix[mid][len(matrix[0]) - 1]:
                top = mid + 1
            else:
                bot = mid - 1
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[mid][m]:
                return True
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                l = m + 1
        return False

