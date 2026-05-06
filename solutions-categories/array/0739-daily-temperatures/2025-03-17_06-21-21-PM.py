class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        s = []
        for i in range(len(temperatures)):
            while s and s[-1][0] < temperatures[i]:
                out[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append((temperatures[i], i))
        
        return out

        '''
        s = 73
        
        74 > 73 -> 

        '''
        
            
