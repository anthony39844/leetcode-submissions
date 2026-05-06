class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums = sorted(nums)
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            m, r = l + 1, len(nums) - 1
            while m < r:
                if nums[l] + nums[m] > nums[r]:
                    break
                tot = nums[l] + nums[m] + nums[r]
                if tot == 0:
                    out.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                elif tot > 0:
                    r -= 1
                else:
                    m += 1
        
        s = set()
        for i in out:
            s.add(tuple(i))

        return list(s)


