class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        for i in arr1:
            while i > 0:
                s.add(i)
                i = i // 10

        out = 0
        for j in arr2:
            while j > 0:
                if j in s:
                    out = max(out, len(str(j)))
                j = j // 10
        return out
