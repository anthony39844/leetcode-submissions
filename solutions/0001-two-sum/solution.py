class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if nums[i] in d:
                return [i, d[nums[i]]]
            d[x] = i
