class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1 
        if haystack == needle:
            return 0
        
        l, r = 0, 0
        
        while l < len(haystack) and r < len(haystack):
            if haystack[l] != needle[0]:
                l += 1
                continue
            else:
                # start of a occurence
                # loop until not same or end and compare
                r = l
                print(haystack[r], needle[r-l])
                while r < len(haystack) and r-l < len(needle) and haystack[r] == needle[r-l]:
                    r += 1
                if haystack[l:r] == needle:
                    return l
                print(haystack[l:r])
                l += 1
        
        return -1

