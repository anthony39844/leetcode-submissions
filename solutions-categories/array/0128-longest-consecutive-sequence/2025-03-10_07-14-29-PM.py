class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        s = set(nums)
        for i in s:
            num = i
            count = 1
            if num - 1 not in s:
                while num + 1 in s:
                    count += 1
                    num += 1
                m = max(m, count)
        return m
            
            

                
