class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        st = []
        st2 = []
        for i in s:
            if i.isalnum():
                st.append(i)
    
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                st2.append(s[i])
        
        return st == st2

