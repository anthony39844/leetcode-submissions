class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        
        '''
        if num1 == "0" or num2 == "0":
            return "0"
        out = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                x = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)  
                s = x + out[i + j + 1]
                print(num1[i], num2[j], x, s) 
                out[i + j + 1] = s % 10
                out[i + j] += s // 10
        
        return ''.join(map(str, out)).lstrip('0')
