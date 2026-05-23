class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        out = []

        def backtrack(idx, arr, remaining):
            if remaining < 0 or idx >= len(nums):
                return

            if remaining == 0:
                out.append(list(arr))
            
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(i, arr, remaining - nums[i])
                arr.pop()

        backtrack(0, [], target)
        return out
