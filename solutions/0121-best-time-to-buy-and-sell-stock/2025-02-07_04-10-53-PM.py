class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        low = prices[0]
        high = prices[0]
        for p in prices:
            if p < low:
                low = p
            out = max(out, p - low)
        return out
