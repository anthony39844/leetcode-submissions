class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        out = []
        def backtrack(arr, remaining):
            if len(arr) == len(nums):
                out.append(arr.copy())
                return
            
            for i in range(len(remaining)):
                backtrack(arr + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return out
