class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a dictionary to store the occurences of each element
        
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1 

        x = [key for key,value in d.items() if value in sorted(list(d.values()), reverse=True)[:k]]

        return x
        
