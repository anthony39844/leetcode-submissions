class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        def backtrack(index, subset):
            if sum(subset) == target:
                out.append(subset.copy())
            elif sum(subset) < target:
                for i in range(index, len(candidates)):
                    subset.append(candidates[i]) 
                    backtrack(i, subset)
                    subset.pop()


        backtrack(0, [])
        return out
