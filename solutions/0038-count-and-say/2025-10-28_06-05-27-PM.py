class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        def convert(arr):
            out = []
            for count, num in arr:
                out.append(str(count))
                out.append(str(num))
            return "".join(out)
        
        def RLE(num):
            out = []
            while num > 0:
                count = 1
                x = num % 10
                num = num // 10
                while num % 10 == x:
                    count += 1
                    num = num // 10
                out.append([count, x])
            return out[::-1]
        
        i = 1
        for _ in range(1, n):
            x = RLE(int(i))
            i = convert(x)
        
        return i
            
        
        
