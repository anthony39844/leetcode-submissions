class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        p = []
        for i in range(len(position)):
            p.append((position[i], speed[i]))
        
        p = sorted(p)
        for i in range(len(p) - 1, -1, -1):
            time = (target - p[i][0]) / p[i][1]
            if s and time <= (target - s[-1][0]) / s[-1][1]:
                s[-1] = min(p[i], s[-1], key=lambda x:x[1])
            else:
                s.append(p[i])
            
        return len(s)
