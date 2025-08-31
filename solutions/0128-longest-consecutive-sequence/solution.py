class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        x = set(nums)
        out = 1
        for i in x:
            count = 1
            if i - 1 not in x:
                while i + 1 in x:
                    count += 1
                    i += 1
                out = max(count, out)
        
        return out

