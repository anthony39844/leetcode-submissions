class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                return abs(i)
            nums[idx] *= -1

        


