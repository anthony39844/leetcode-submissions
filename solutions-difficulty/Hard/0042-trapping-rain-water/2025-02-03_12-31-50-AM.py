class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        tot = 0
        maxL, maxR = height[0], height[-1]
        while l < r:
            if maxL <= maxR:
                if maxL - height[l] > 0:
                    tot += maxL - height[l]
                l += 1
            elif maxL > maxR:
                if maxR - height[r] > 0:
                    tot += maxR - height[r]
                r -= 1
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)
        
        return tot
            
            

