class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        p = []
        for i in range(len(position)):
            p.append((position[i], speed[i]))
        p = sorted(p)

        for i in range(len(p) - 1, -1, -1):
            x, sp = p[i]
            time = (target - x) / sp
            if s:
                if time > s[-1]:
                    s.append(time)
            else:
                s.append(time)
            
        return len(s)
