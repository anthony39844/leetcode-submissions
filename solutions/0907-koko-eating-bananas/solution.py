class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            count = 0
            mid = (l + r) // 2
            for i in piles:
                count += math.ceil(i/mid)
            if count <= h:
                res = min(mid, res)
                r = mid - 1
            elif count > h:
                l = mid + 1
        return res

