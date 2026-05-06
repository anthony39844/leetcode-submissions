class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        arr = []

        def backtrack(arr, i):
            if sum(arr) == target:
                out.append(arr.copy())
                return
            if sum(arr) > target:
                return

            while i < len(candidates):
                arr.append(candidates[i])
                backtrack(arr, i)
                arr.pop()
                i += 1

        backtrack([], 0)

        return out
