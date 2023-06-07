class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for x in nums:
            new_set.add(x)
        if len(nums) != len(new_set):
            return True
        else:
            return False
