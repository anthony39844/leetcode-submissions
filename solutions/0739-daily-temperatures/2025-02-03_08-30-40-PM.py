class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        s = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            while temperatures[i] > s[-1][0]:
                x = s.pop()[1]
                out[x] = i - x
                if not s:
                    s.append((temperatures[i], i))
            else:
                s.append((temperatures[i], i))
        return out
            
