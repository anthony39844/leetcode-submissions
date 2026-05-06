class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        h = Counter(nums)

        def backtrack(arr):
            if len(arr) == len(nums):
                out.append(arr.copy())
                return
            for x, count in h.items():
                if count > 0:
                    arr.append(x)
                    h[x] -= 1
                    backtrack(arr)
                    h[x] += 1
                    arr.pop()
        backtrack([])
        return out

