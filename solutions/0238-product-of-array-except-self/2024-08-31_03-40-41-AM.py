class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        out = []
        for i in nums:
            out.append(l) 
            l *= i
        print(out)
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= r
            r *= nums[i]
    
        return out
