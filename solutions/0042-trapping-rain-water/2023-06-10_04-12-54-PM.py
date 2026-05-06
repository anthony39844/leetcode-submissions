class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0 
        left = 0
        right = len(height) - 1
        maxL, maxR = height[left], height[right]
        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                total += maxL - height[left]
            else:
                right -= 1
                maxR = max(maxR, height[right])
                total += maxR - height[right]
        return total
        
            
        


