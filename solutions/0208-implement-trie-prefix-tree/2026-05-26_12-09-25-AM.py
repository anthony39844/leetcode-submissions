# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end = False

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
            
        cur["end"] = True

    def search(self, word: str) -> bool:
        cur = self.root 
        for i in word:
            if i in cur:
                cur = cur[i]
            else:
                return False
      
        return "end" in cur and cur["end"]
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for i in prefix:
            if i in cur:
                cur = cur[i]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
