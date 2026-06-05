class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # not possible to get to the endWord
        if endWord not in wordList:
            return 0

        # create a map of all wildcards to the words they match O(n * l)
        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                d[word[:i] + "*" + word[i+1:]].append(word)
                
        out = 0
        q = deque([(beginWord)])
        visited = {beginWord}

        # bfs
        while q:
            out += 1

            for _ in range(len(q)):

                word = q.popleft()
                if word == endWord:
                    return out
    
                for i in range(len(word)):
                    wildcard = word[:i] + "*" + word[i+1:]
                    for x in d[wildcard]:
                        if x not in visited:
                            q.append(x)
                            visited.add(x)

        # q became empty and we never found the word, not possible
        return 0
        

