class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []

        def backtrack(x, arr, total):
            if total == target:
                out.append(arr.copy())
                return
            if total > target:
                return
            
            for i in range(x, len(candidates)):
                if i != x and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(i + 1, arr, total + candidates[i])
                arr.pop()
        
        backtrack(0, [], 0)
        return out
