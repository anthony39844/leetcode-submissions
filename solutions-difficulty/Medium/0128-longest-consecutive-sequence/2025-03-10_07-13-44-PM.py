class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        s = set(nums)
        count = 1
        for i in s:
            num = i
            if num - 1 not in s:
                while num + 1 in s:
                    count += 1
                    num += 1
            m = max(m, count)
            count = 1
        return m
            
            

                
