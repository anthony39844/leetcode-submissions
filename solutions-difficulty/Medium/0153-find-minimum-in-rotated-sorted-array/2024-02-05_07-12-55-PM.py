class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                break
        if i == len(nums) - 1:
            if nums[i] > nums[0]:
                return nums[0]
            else:
                return nums[i]
        else:
            return nums[i]
