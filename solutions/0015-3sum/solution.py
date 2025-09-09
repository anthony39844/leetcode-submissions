class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = len(nums) - 1
            j = i + 1
            while j < k:
                x = nums[i] + nums[j] + nums[k]
                if x == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif x < 0:
                    j += 1
                else:
                    k -= 1

        return out

