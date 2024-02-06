class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]


        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i - 1]:
        #         break
        # if i == len(nums) - 1:
        #     if nums[i] > nums[0]:
        #         return nums[0]
        #     else:
        #         return nums[i]
        # else:
        #     return nums[i]
