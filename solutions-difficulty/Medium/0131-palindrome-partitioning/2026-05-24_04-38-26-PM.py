class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def check(st):
            return st == st[::-1]

        def backtrack(idx, arr):
            
            if idx == len(s):
                out.append(list(arr))
                return

            for i in range(idx, len(s)):
                if check(s[idx:i+1]):
                    arr.append(s[idx:i+1])
                    backtrack(i + 1,  arr)
                    arr.pop()
                
        backtrack(0, [])
        return out
