class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                pass
            else: 
                nums_dict[i] = nums.count(i)
        sorted_dict = dict(sorted(nums_dict.items(), key=lambda x: x[1], reverse = True))
        nums_list = list(sorted_dict.keys())
        return nums_list[:k]
