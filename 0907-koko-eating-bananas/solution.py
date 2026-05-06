class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        l, r = 1, piles[-1]
        out = float('inf')

        while l <= r:
            t = 0
            k = (l + r) // 2

            for i in piles:
                t += math.ceil(i / k)
            if t <= h:
                out = min(out, k)
            else:
                l = k + 1
                continue
            r = k - 1

        return out
