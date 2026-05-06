class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }
        out = []
        path = []

        def backtrack(ind):
            if ind >= len(digits):
                out.append("".join(path))
                return
  
            for char in mapping[digits[ind]]:
                path.append(char)
                backtrack(ind + 1)
                path.pop()
                
        backtrack(0)
        return out
