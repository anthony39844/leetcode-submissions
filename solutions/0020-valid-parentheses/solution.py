class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if len(s) % 2 == 1:
            return False
        open_p = {"(" : ")", "[" : "]", "{" : "}"}
        for i in s:
            if i in open_p:
                st.append(open_p[i])
            else:
                if not st or not i == st.pop():
                    return False

        return len(st) == 0
