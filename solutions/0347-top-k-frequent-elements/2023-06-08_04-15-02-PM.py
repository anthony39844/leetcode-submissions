from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_counter = Counter(nums)
        nums_list = list([value for value, count in my_counter.most_common(k)])
        print(nums_list)
        return nums_list
