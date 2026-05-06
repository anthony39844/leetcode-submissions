class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a dictionary to store the occurences of each element
        
        d = {}
        out = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        topK = [key for key, value in sorted(list(d.items()), key=lambda x:x[1], reverse=True)[:k]]

        return topK
