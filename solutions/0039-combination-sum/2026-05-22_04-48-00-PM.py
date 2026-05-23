class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        out = []

        def backtrack(idx, arr, total):
            if total > target or idx >= len(nums):
                return

            if total == target:
                out.append(list(arr))
            
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(i, arr, total + nums[i])
                arr.pop()

        backtrack(0, [], 0)
        return out
