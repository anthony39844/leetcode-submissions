class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        out = 0

        # so the remaining stack will be calculated
        heights.append(0)

        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]:
                x = s.pop()

                # no left bar is shorter
                if not s:
                    w = i
                else: # s[-1] is the left boundary of this bar we popped
                    w = i - s[-1] - 1
                
                out = max(out, heights[x] * w)
            
            s.append(i)
    
        return out
                

