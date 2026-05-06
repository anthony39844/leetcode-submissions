class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        s = set()
        
        def backtrack(current):
            if len(current) == len(nums):
                out.append(current.copy())

            for i in range(len(nums)):
                if i not in s:
                    s.add(i)
                    backtrack(current + [nums[i]])
                    s.remove(i)
            
        backtrack([])
        return out
