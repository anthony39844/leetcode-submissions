class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            want = target - nums[i]
            if want in d:
                return [d[want], i]
            else:
                d[nums[i]] = i
