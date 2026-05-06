class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        out = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else: #prices[r] > prices[l]
                out = max(out, prices[r] - prices[l])
                r += 1
        return out
