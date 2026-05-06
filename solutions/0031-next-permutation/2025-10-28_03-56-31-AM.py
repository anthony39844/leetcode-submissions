class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums.reverse()
            return
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                l = i + 1
                swap = l
                while l < len(nums):
                    if nums[l] > nums[i] and nums[l] < nums[swap]:
                        swap = l
                    l += 1
                nums[swap], nums[i] = nums[i], nums[swap]
                print(nums, nums)
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.reverse()
        return
            
        
        



