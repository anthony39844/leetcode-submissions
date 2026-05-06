class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]

        out = []
        for i in d:
           out.append(d[i]) 
        return out

