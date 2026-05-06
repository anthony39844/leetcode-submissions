class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        time = o(2^n)
        space = o(n)
        '''
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
                if candidates[i] > target:
                    break
                backtrack(i + 1, arr + [candidates[i]], total + candidates[i])
        
        backtrack(0, [], 0)
        return out
