class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        min = prices[0]
        for i in prices[1:]:
            if i < min:
                min = i
            if i - min >= diff:
                diff = i - min
             
        return diff
        
