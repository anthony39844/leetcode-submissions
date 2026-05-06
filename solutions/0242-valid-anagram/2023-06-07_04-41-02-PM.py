class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for x in s:
            s_dict[x] = s_dict.get(x, 0) + 1
        for x in t:
            t_dict[x] = t_dict.get(x, 0) + 1
        return s_dict == t_dict
