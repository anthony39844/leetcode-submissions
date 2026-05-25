class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []

        def check(st):
            l, r = 0, len(st) - 1
            while l < r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True

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
