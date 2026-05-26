class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
            
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root 
        for i in word:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
      
        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for i in prefix:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
