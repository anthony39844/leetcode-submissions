class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        tot = 0
        maxL, maxR = height[0], height[-1]
        while l < r:
            if maxL <= maxR:
                tot += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                tot += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])

        return tot
