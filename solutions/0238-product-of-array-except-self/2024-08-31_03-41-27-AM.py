class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]

        for i in range(1, len(nums)): 
            out.append(out[i - 1] * nums[i - 1])
            # [1, 2, 3, 4]
            # out = [1] loop
            # out = [1, 1*1] loop i = 1
            # out = [1, 1, 1*2] loop i = 2
            # out = [1, 1, 2, 2*3] i = 3
        #so this loop makes an array with product of the elements to the left of the index

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= right
            right *= nums[i]

            # out = [1, 1, 2, 6]
            # out = [1, 1, 2, 6*1] i = 3, right = 4
            # out = [1, 1, 2*4, 6] i = 2, right = 12
            # out = [1, 1*12, 8, 6] i = 1, right = 24
            # out = [1*24, 12, 8, 6] i = 0, right = 24
            # out = [24, 12, 8, 6] end loop
        # this loop multiplies the index with the product of the elements to the right of it
        return out
