class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = 0
        l = 0
        se = set()
        for i in range(len(s)):
            while s[i] in se: #while there is a repeat char, remove the left most char of the string from the set until its s[r] is no longer a repeat
                se.remove(s[l])
                l += 1
            se.add(s[i]) 
            x = max(x, i - l + 1) # + 1 to be inclusive
        
        return x
            
