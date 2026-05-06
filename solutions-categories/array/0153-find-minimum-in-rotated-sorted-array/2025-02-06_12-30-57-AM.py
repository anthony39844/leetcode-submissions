class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        cur = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(cur, nums[l])

            mid = (l + r) // 2 
            cur = min(cur, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return cur
