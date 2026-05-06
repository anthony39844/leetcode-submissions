class Solution:
    def maxArea(self, height: List[int]) -> int:
        #  (r - l) * (min((height[l], height[r])))

        l = 0
        r = len(height) - 1
        out = 0 
        while l <= r:
            area = (r - l) * (min(height[l], height[r]))
            out = max(out, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return out
            
