class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2, 7, 11, 15
        # we use the keys as values we need and the value as the value we are at

        d = {}
        for i, j in enumerate(nums):
            x = target - j
            if j in d:
                return [i, d[j]]
            else:
                d[x] = i

