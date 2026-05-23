class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []

        def backtrack(idx, arr, remaining):
            if remaining < 0:
                return

            if remaining == 0:
                out.append(list(arr))
            
            for i in range(idx, len(nums)):
                if nums[i] > remaining:
                    break
                arr.append(nums[i])
                backtrack(i, arr, remaining - nums[i])
                arr.pop()

        backtrack(0, [], target)
        return out
