class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(speed):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / mid)
            return hours <= h

        if h == len(piles):
            return max(piles)

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid): #if koko can finish then decrease the k
                right = mid
            else: #if not increase the k
                left = mid + 1
        return left

             

       
