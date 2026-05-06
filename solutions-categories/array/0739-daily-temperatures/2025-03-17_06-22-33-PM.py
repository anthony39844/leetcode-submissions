class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        s = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            while s and s[-1][0] < temperatures[i]:
                out[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append((temperatures[i], i))
        
        return out
        
            
