class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for x in s:
            s_dict[x] = s.count(x)
        for x in t:
            t_dict[x] = t.count(x)
        return s_dict == t_dict
