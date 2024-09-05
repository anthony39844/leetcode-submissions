class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        l = 1
        for i in nums:
            out.append(l)
            l *= i
        
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= r
            r *= nums[i]

        return out

