class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        
        '''
        a = 0
        b = 0
        for count, num in enumerate(reversed(num1)):
            x = ord(num) - 48
            a += x * (10 ** count)
        for count, num in enumerate(reversed(num2)):
            x = ord(num) - 48
            b += x * (10 ** count)

        return str(a * b)
        

