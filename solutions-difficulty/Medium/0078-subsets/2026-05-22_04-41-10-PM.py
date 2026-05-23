class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        
        def backtrack(idx, arr):
            # Every combination we generate along the way is a valid subset, 
            # so we append a copy of it immediately.
            out.append(list(arr))
            
            for i in range(idx, len(nums)):
                # 1. Choose: Include the current element
                arr.append(nums[i])
                
                # 2. Explore: Move forward to the next index (i + 1)
                backtrack(i + 1, arr)
                
                # 3. Un-choose: Pop it out (backtrack) to try the next number
                arr.pop()

        backtrack(0, [])
        return out
