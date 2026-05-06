class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outer_list = []
        nums_dict = dict()
        sorted_nums = sorted(nums)
        for i, mid in enumerate(sorted_nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if mid + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                elif mid + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                else:
                    inner_list = [mid, sorted_nums[left], sorted_nums[right]]
                    key = tuple(inner_list)
                    if key not in nums_dict:
                        outer_list.append(inner_list)
                        nums_dict[key] = 1 
                    inner_list = []
                    left += 1
        return outer_list
