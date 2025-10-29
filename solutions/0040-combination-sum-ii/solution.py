class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        time = o(2^n)
        space = o(n)
        '''
        candidates.sort()
        out = []

        def backtrack(x, arr, t):
            if t < 0:
                return
            if t == 0:
                out.append(arr.copy())
                return
            
            for i in range(x, len(candidates)):
                if i != x and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > t:
                    break
                backtrack(i + 1, arr + [candidates[i]], t - candidates[i])
        
        backtrack(0, [], target)
        return out
