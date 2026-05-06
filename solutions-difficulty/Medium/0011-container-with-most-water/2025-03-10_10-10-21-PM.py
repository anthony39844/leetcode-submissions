class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        m = 0
        while l < r:

            vol = (r - l) * min(height[l], height[r])
            m = max(vol, m)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return m
