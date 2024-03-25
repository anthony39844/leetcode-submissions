class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            val = target - nums[i]
            if val in d and i != d[val]:
                return [i, d[val]]
                
        
        
