class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        visited = set()
        def backtrack(idx, arr):

            if len(arr) == len(nums):
                out.append(list(arr))
                return
            
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue 
                arr.append(nums[i])
                visited.add(nums[i])
                backtrack(i + 1, arr)
                arr.pop()
                visited.remove(nums[i])
        
        backtrack(0, [])
        return out
