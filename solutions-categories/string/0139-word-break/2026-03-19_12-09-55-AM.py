class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def func(st, x):
            if st == "":
                return True
            else:
                if st.startswith(x):
                    st = st[len(x):]
                    for w in wordDict:
                        if func(st, w):
                            return True
            return False

        for w in wordDict:
            if func(s, w):
                return True

        return False
