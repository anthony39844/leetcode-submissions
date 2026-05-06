class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        out = []
        def backtrack(arr):
            if len(arr) == len(nums):
                out.append(arr.copy())
                return
            
            for i in nums:
                if i not in arr:
                    arr.append(i)
                    backtrack(arr)
                    arr.pop()

        backtrack([])
        return out
