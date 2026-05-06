class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev = 0
        prev2 = nums[0]
        cost = 0
        for i in range(1, len(nums)):
            cost = max(prev2, prev + nums[i])
            prev, prev2 = prev2, cost

        return cost

