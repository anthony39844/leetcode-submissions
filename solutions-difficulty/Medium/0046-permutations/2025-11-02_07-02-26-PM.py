class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        time = o(n! * n^2)
        space = o(n)
        '''
        out = []
        used = [False] * len(nums)
        def backtrack(arr):
            if len(arr) == len(nums):
                out.append(arr.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    arr.append(nums[i])
                    backtrack(arr)
                    arr.pop()
                    used[i] = False

        backtrack([])
        return out
