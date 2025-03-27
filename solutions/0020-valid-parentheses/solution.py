class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_p = {'(': ')', '{': '}', '[': ']'}

        for i in s:
            if i in open_p:
                st.append(open_p[i])
            else:
                if not st or st.pop() != i:
                    return False
        
        return len(st) == 0
