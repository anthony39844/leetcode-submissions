class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                st.append(i)

        if st == st[::-1]:
            return True
        else:
            return False
