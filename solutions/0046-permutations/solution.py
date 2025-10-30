class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        time = o()
        space = o(n)
        '''
        out = []
        used = [False] * len(nums)
        def backtrack(arr):
            if len(arr) == len(nums):
                out.append(arr[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    backtrack(arr + [nums[i]])
                    used[i] = False

        backtrack([])
        return out
