class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:  
        out = [0] * len(temperatures)
        s = []
        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                index = s.pop()
                out[index] = i - index
            s.append(i)
        return out

        # out = []
        # s = []
        # for i in range(len(temperatures) - 1):
        #     s.append(temperatures[i + 1])
        #     if temperatures[i] < temperatures[i + 1]:
        #         out.append(len(s))
        #         s = []
        #     else:
        #         j = i + 1
        #         while temperatures[j] <= temperatures[i]:
        #             j += 1
        #             if j >= len(temperatures):
        #                 break
        #             s.append(temperatures[j])
        #         if j >= len(temperatures):
        #             out.append(0)
        #         else:
        #             out.append(len(s))
        #         s = []
        # out.append(0)
        # return out




        
