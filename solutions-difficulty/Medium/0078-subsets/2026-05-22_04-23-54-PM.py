class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        
        def backtrack(arr, i):
            if i >= len(nums):
                return
            
            for x in range(i, len(nums)):
                if nums[x] in arr:
                    continue
                a = arr + [nums[x]]
                out.append(a)
                backtrack(a, x)
                

        
        backtrack([], 0)
        return out
            
