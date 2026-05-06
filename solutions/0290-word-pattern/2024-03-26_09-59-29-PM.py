class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split(" ")
        if len(strs) != len(pattern):
            return False
        hash = {}
        for i in range(len(pattern)):
            if pattern[i] in hash or strs[i] in hash.values():
                continue
            else:
                hash[pattern[i]] = strs[i]
        print(hash)
        for i in range(len(pattern)):
            if pattern[i] not in hash or hash[pattern[i]] != strs[i]:
                return False
        return True
