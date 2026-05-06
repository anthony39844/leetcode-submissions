class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, mini = 0, 100000
        for i in prices:
            if i < mini:
                mini = i
            if i - mini > profit:
                profit = i - mini
        return profit

