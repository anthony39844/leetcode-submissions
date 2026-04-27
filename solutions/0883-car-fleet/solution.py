class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p, s = zip(*sorted(zip(position, speed), reverse=True))
        p, s = list(p), list(s)
        st = []
        for i, x in enumerate(p):
            t = ((target - x) / s[i])
            if st and st[-1] >= t:
                continue
            st.append(t)

        return len(st)



