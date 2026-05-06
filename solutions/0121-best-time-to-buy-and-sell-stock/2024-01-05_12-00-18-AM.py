class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        min = 1000000
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
             
            if prices[i] - min >= diff:
                diff = prices[i] - min
             
        return diff
        
