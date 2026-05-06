class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if h == len(piles):
            return max(piles)
        right, left = max(piles), 1
        mid = 0
        while left < right:
            hour = 0
            mid = left + (right - left) // 2
            for i in piles:
                hour += ceil(i / mid)
            if hour <= h:
                right = mid #there is a smaller k
            elif hour > h:
                left = mid + 1
        return left 

             

       
