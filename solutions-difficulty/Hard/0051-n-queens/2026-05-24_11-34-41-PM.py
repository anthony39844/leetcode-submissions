class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(r, arr):
            if r == n:
                out.append(list(arr))
            
            for i in range(n):
                d1 = r - i
                d2 = r + i
                if i in cols or d1 in diag1 or d2 in diag2:
                    continue

                cols.add(i)
                diag1.add(r - i)
                diag2.add(r + i)
                s = "." * i + "Q" + "." * (n - i - 1)
                arr.append(s)
                backtrack(r + 1, arr)
                arr.pop()
                cols.remove(i)
                diag1.remove(r - i)
                diag2.remove(r + i)      


        backtrack(0, [])
        return out
