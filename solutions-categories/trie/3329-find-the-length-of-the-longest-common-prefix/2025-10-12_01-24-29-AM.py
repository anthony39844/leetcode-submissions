class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        for i in arr1:
            while i not in s and i > 0:
                s.add(i)
                i = i // 10

        out = 0
        for j in arr2:
            while j not in s and j > 0:
                j = j // 10
            
            if j: out = max(out, len(str(j)))
        return out
