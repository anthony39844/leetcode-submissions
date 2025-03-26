class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            
        if h == len(piles):
            return max(piles)
            
        l, r = 1, max(piles)
        cur_k = r
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            if time <= h:
                # this wont go past the minimum bc if it goes past the min k then it will take more time than h
                cur_k = min(cur_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return cur_k



