class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        most = 0
        while l < r:
            x = min(height[l], height[r]) * (r - l)
            most = max(most, x)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return most
