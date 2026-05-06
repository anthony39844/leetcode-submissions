class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                return i
            else:
                d[i] = 1

        # d = {}
        # for i in nums:
        #     d[i] = d.get(i, 0) + 1
        # for i in d:
        #     if d[i] > 1:
        #         return i


        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]

