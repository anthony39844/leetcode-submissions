class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def backtrack(i, curr):
            out.append(curr.copy())
            for i in range(i, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return out

