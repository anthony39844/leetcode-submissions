class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        p = {')': '(', '}': '{',  ']': '['}

        for i in s:
            if i in p:
                if not st or st.pop() != p[i]:
                    return False
            else:
                st.append(i)
        return st == []
