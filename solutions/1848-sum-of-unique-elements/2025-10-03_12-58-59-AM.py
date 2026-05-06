class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = set()
        o = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                o.add(i)
        return sum(s) - sum(o)
