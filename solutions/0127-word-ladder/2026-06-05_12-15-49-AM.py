class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        d = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                d[word[:i] + "*" + word[i+1:]].append(word)
                
        out = 0
        q = deque([(beginWord)])
        visited = {beginWord}

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

        return 0
        

