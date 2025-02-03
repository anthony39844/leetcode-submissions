class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        s = set(nums)
        for i in s:
            cur_len = 1
            cur = i
            if i - 1 not in s:
                while cur + 1 in s:
                    cur += 1
                    cur_len += 1
                m = max(m, cur_len)
        return m
            

                
