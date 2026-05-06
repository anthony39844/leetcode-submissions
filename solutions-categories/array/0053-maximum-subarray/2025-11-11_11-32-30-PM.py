class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cur, out = 0, nums[0]

        for i in nums:
            cur = max(i, cur + i)
            out = max(out, cur)
    
        return out

