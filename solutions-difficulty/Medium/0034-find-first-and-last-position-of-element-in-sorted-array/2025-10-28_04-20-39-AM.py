class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        out = []
        l, r = 0, len(nums) - 1
        while l <= r:
            x = (l + r) // 2
            if nums[x] == target:
                l, r = x, x
                while l >= 0 and nums[l] == target:
                    l -= 1
                while r < len(nums) and nums[r] == target:
                    r += 1
                return [l + 1, r - 1]
            elif nums[x] > target:
                r -= 1
            else:
                l += 1

        return [-1, -1]
