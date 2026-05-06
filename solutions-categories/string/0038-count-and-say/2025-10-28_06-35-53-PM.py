class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        time = o(kn)
        space = o(kn)
        '''
        if n == 1:
            return "1"

        
        def RLE(s):
            out = []
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    out.append(str(count))
                    out.append(s[i-1])
                    count = 1
            
            out.append(str(count))
            out.append(s[-1])
            return "".join(out)
        
        i = "1"
        for _ in range(1, n):
            i = RLE(i)
        
        return i
            
        
        
