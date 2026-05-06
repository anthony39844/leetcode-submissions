class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l, r = 0, len(nums) - 1
\
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
            print(m)
            if nums[m] < nums[r] and m > 0 and nums[m] < nums[m - 1]: # we know the right side is increasing and m is smallest 

                return nums[m]
            elif nums[m] < nums[r]: #right side increasing, but pivot is still on the left
                r = m - 1
            else: # we know the pivot is on the left
                l = m + 1

        return nums[m]
