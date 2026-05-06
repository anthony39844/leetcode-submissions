class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            small = min(height[left], height[right])
            distance = right - left
            area = small * distance
            if area >= maxArea:
                maxArea = area
            if height[left] == small:
                    left += 1
            elif height[right] == small:
                    right -= 1
        return maxArea

