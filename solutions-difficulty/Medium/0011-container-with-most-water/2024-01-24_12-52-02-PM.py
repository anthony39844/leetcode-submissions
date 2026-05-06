class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, water = 0 , len(height) -1, 0
        while left < right:
            vol = (right - left) * min(height[left], height[right])
            water = max(water, vol)
            if height[left] >= height[right]:
                right -= 1
            else: 
                left += 1
        return water
            
