class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        current = []
        
        def backtrack(start, current):
            for i in range(start, len(nums)):
                current.append(nums[i])
                out.append(current.copy())
                backtrack(i + 1, current)  # Pass i + 1 to avoid using the same element again
                current.pop()

        
        backtrack(0, [])
        return out


        
