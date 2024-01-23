class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        length = 1
        maxl = 1
        for i in nums:
            if i - 1 not in nums:
                while i + 1 in nums:
                    i += 1
                    length += 1
            if length > maxl:
                maxl = length
                length = 1
            else:
                length = 1
        return maxl

        
        
