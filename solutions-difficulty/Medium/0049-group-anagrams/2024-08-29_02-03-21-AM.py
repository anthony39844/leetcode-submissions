class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        out = []
        for i in strs:
            s = "".join(sorted(i))
            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)
        for i in d:
            out.append(d[i])
        return out

