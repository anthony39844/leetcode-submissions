class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        out = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        topK = sorted(list(d.items()), key=lambda x:x[1], reverse=True)[:k]
        print(topK)
        for i in topK:
            out.append(i[0])
        return out 
            

