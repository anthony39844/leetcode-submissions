class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        print(candidates)
        def backtrack(idx, arr, remaining):
            if remaining < 0:
                return
            
            if remaining == 0:
                out.append(list(arr))
            
            for i in range(idx, len(candidates)):
                # if same number and not the first instance of it we continue (makes dup combos)
                if idx != i and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                arr.append(candidates[i])
                backtrack(i + 1, arr, remaining - candidates[i])
                arr.pop()

        backtrack(0, [], target)
        return out
