class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates to avoid duplicate combinations
                if target - candidates[i] >= 0:
                    path.append(candidates[i])
                    backtrack(i + 1, target - candidates[i], path)
                    path.pop()

        candidates.sort()  # Sort candidates to handle duplicates
        result = []
        backtrack(0, target, [])
        return result
        
