class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        '''
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        out = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i + 1]]:
                out += (mapping[s[i + 1]] - mapping[s[i]])
                i += 2
            else:
                out += mapping[s[i]]
                i += 1
        
        return out
            
