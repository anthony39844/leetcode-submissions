class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s = set()
        for i in arr1:
            a = i
            while a > 0:
                s.add(a)
                a = a // 10

        out = 0
        for j in arr2:
            b = j
            while b > 0:
                if b in s:
                    out = max(out, len(str(b)))
                b = b // 10
        return out
