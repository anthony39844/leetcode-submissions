class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
 
        out = []
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for j in range(len(strs)):
                if shortest[i] == strs[j][i]:
                    continue
                else:
                    return "".join(out)
            out.append(shortest[i])
        return "".join(out)
