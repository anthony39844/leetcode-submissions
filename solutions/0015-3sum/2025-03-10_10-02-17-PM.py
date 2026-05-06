class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums = sorted(nums)
        for l in range(len(nums)):
            m, r = l + 1, len(nums) - 1
            while m < r:
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


