class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        out = []
        for i in range(k):
            cur = list(d.keys())[list(d.values()).index(max(d.values()))]
            out.append(cur)
            del d[cur]  

        return out      

