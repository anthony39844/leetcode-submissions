class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]

        for i in range(1, len(nums)):
            out.append(out[i - 1] * nums[i - 1])
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= right
            right *= nums[i]
        return out
        
        # out = []
        # ltotal = 1
        # rtotal = 1
        # for i in range(len(nums)):
        #     left = 0
        #     right = len(nums) - 1
        #     while left < i:
        #         ltotal *= nums[left]
        #         left += 1
        #     while right > i:
        #         rtotal *= nums[right]
        #         right -= 1
        #     out.append(rtotal * ltotal)
        #     rtotal = 1
        #     ltotal = 1
        # return out

     

