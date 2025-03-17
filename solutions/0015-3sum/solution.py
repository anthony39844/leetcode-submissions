class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot == 0:
                    out.append((nums[i], nums[j], nums[k]))
                    j += 1
                elif tot < 0:
                    j += 1
                else:
                    k -= 1
        
        s = list(set(out))

        return s

