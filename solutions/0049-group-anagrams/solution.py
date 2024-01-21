class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        answer = []
        for i in strs:
            sort = ''.join(sorted(i))
            if sort not in map:
                map[sort] = []
            map[sort].append(i)
        
        for val in map.values():
            answer.append(val)
        return answer
            
