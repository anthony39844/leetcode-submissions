class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        out = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        for val in d:
            out.append(val[0])
            if len(out) == k:
                return out

            
