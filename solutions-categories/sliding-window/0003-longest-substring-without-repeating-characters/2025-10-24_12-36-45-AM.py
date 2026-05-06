class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        st = set()
        out = 0
        l, r = 0, 0
    
        while r < len(s):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            out = max(len(st), out)
            r += 1
        return out


                    




