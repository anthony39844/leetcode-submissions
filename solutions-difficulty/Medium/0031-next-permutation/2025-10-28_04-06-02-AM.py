class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        time = o()
        '''
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums.reverse()
            return
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                swap = len(nums) - 1
                while swap > i:
                    if nums[swap] > nums[i]:
                        break
                    swap -= 1
                nums[swap], nums[i] = nums[i], nums[swap]
                nums[i+1:] = nums[i+1:][::-1]
                return
        nums.reverse()
        return
            
        
        



