class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        time = 
        space = 
        '''

        out = []
        arr = []

        def backtrack(arr, x, total):
            if total == target:
                out.append(arr.copy())
                return
            if total > target:
                return

            for i in range(x, len(candidates)):
                arr.append(candidates[i])
                backtrack(arr, i, total + candidates[i])
                arr.pop()

        backtrack([], 0, 0)

        return out
