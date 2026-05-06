class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        out = 0

        for i in range(len(heights)):
            start = i
            while s and s[-1][0] > heights[i]:
                h, ind = s.pop()
                out = max(out, h * (i - ind))
                start = ind
            s.append([heights[i], start])
        
        i += 1

        for _ in range(len(s) - 1, -1, -1):
            h, ind = s.pop()
            out = max(out, h * (i - ind))
        
        return out
