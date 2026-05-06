class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            x = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if x == target:
                return True
            elif x < target:
                l += 1
            else:
                r -= 1
        return False

