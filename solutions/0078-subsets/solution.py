class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        current = []
        
        def backtrack(start, current):
            out.append(current.copy())  # Add a copy of the current subset to the result
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)  # Recursive call with the next index
                current.pop()  # Backtrack by removing the last element

        backtrack(0, [])  # Start backtracking with an empty subset
        return out

        
