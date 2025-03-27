class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1 5 3 6 4
        # 7 1
        #.  1 5 = 4
        #.  1   3 6 


        l = 0
        profit = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            elif prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
        
        return profit
            
