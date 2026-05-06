class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        s = set(nums)
        for i in s:
            count = 1
            if i + 1 not in s:
                while i - 1 in s:
                    count += 1
                    i -=1
            m = max(count, m)
        return m
            
            

                
