class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        for i in nums:
            dictionary[i] = dictionary.get(i, 0) + 1

        return any(value > 1 for value in dictionary.values())




        
