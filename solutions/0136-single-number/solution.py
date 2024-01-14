class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = 0
        for num in nums:
            c ^= num
        return c
        


        
