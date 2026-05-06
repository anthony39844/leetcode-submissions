class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        out = nums[0]
        while l <= r:
            m = (l + r) // 2
            out = min(out, nums[m])
            if nums[r] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return out
