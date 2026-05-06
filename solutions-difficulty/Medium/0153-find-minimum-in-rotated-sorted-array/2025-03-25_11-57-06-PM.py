class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums) - 1
        #  if nums[m] < nums[r] go left
        # if 
        '''
        1 2 3 4 5 
        5 1 2 3 4
        4 5 1 2 3
        3 4 5 1 2 
        2 3 4 5 1
        '''

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[r] and nums[m] < nums[m - 1]:
                return nums[m]
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        return nums[m]
