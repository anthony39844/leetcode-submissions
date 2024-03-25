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

