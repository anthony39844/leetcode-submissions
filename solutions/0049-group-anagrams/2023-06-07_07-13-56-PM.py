class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
        # Sort the string and use it as a key in the hashmap
            sorted_str = ''.join(sorted(s))

        # If the sorted string is already in the hashmap, append the original string to its value
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(s)
                print(anagram_map[sorted_str])
            else:
            # If the sorted string is not in the hashmap, create a new key-value pair
                anagram_map[sorted_str] = [s]
        grouped_anagrams = list(anagram_map.values())
        return grouped_anagrams

