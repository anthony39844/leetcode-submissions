class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur["end"] = True

    def search(self, word: str) -> bool:
        def dfs(idx, cur):
            if idx == len(word):
                return "end" in cur and cur["end"]
            
            if word[idx] == ".":
                for key in cur.keys():
                    if key != "end":
                        if dfs(idx + 1, cur[key]):
                            return True
                return False

            if word[idx] in cur:
                return dfs(idx + 1, cur[word[idx]])

            return False

        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
