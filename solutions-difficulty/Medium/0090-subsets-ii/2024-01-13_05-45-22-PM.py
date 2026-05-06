class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []

        def backtrack(index, sub):
            sub = sorted(sub)
            if sub not in out:
                out.append(sub[:])
            for i in range(index, len(nums)):
                sub.append(nums[i])
                backtrack(i + 1, sub)
                sub.pop()


        backtrack(0, [])
        return out
