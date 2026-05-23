class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        out = []

        def backtrack(idx, arr):
            if sum(arr) > target or idx >= len(nums):
                return

            if sum(arr) == target:
                out.append(list(arr))
            
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(i, arr)
                arr.pop()

        backtrack(0, [])
        return out
