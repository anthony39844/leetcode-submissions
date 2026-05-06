class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height) -1 
        water = 0
        while left < right:
            width = right - left
            vol = width * min(height[left], height[right])
            if vol > water:
                water = vol
            if height[left] >= height[right]:
                right -= 1
            else: 
                left += 1
        return water
            
