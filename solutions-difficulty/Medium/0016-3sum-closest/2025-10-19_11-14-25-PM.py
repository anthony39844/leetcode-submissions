class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        out = sum(nums[:3])
        if out == target:
            return out

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                x = nums[i] + nums[l] + nums[r]
                if abs(target - x) <= abs(target - out):
                    out = x
                
                if x > target:
                    r -= 1
                elif x < target:
                    l += 1
                else:
                    return out
                               
        return out

