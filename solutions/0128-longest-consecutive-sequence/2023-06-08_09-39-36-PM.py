class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sorted_nums = sorted(nums_set)
        longest = 1
        max_long = 0
        if len(nums) == 0:
            return 0
        print(sorted_nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] == 1:
                longest += 1
            else:
                if longest > max_long:
                    max_long = longest
                    longest = 1
                else:
                    longest = 1
        if longest > max_long:
            max_long = longest
        return max_long
            
