class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = 0
        for i in range(1, len(nums) + 1):
            tot += i
        return tot - sum(nums)
        
