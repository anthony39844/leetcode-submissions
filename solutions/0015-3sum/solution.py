class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif tot < 0:
                    l += 1
                else:
                    r -= 1
  
        return out
