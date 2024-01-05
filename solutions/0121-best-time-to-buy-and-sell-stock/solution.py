class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        min = 1000000
        for i in prices:
            if i < min:
                min = i
            if i - min >= diff:
                diff = i - min
             
        return diff
        
