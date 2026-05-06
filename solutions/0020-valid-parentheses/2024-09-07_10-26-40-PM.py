class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        p = {')': '(', '}': '{', ']': '['}
        for i in s:
            print(i)
            if i in p and st:
                x = st.pop()
                if x != p[i]:
                    return False
            else:
                st.append(i)
                
        if st == []:
            return True
        else: 
            return False
