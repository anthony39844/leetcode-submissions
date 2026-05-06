class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
        return list(map(list, set(map(tuple, out))))
