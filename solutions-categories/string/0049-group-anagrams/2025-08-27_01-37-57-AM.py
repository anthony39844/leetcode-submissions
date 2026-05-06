class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each word and then if they are the same then they belong in the same group
        # we can keep a dictionary where the key is the sorted word and the value is a array of words that sort into the key
        d = {}
        out = []
        for i in strs:
            word = str(sorted(i))
            if word in d:
                d[word].append(i)
            else:
                d[word] = [i]

        for key,value in d.items():
            out.append(value)
        return out
