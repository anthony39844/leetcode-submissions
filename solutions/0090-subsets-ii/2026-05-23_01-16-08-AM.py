class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        def backtrack(idx, arr):
            
            out.append(list(arr))
            for i in range(idx, len(nums)):
                if idx != i and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()

        backtrack(0, [])
        return out
