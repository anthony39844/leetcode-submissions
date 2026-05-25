class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        out = []

        def backtrack(i, s):
            if len(s) == len(digits):
                out.append(s)
                return

            letters = d[digits[i]]
            for l in letters:
                backtrack(i + 1, s + l)

        backtrack(0, "")
        return out
