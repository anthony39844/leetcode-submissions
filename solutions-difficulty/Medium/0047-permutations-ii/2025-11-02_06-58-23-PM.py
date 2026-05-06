class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(arr):
            if len(arr) == len(nums):
                out.append(arr.copy())
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    used[i] = True
                    arr.append(nums[i])
                    backtrack(arr)
                    arr.pop()
                    used[i] = False

        backtrack([])
        return out
