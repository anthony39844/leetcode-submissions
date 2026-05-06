class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outer_list = []
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
                    outer_list.append(inner_list)
                    inner_list = []
                    left += 1
        def find_unique_triplets(outer_list):
            unique_triplets = set()
            for sublist in outer_list:
                for triplet in combinations(sublist, 3):
                    unique_triplets.add(tuple(sorted(triplet)))
            return list(unique_triplets)
        return find_unique_triplets(outer_list)
