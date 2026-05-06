class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC",
            400: "CD", 900: "CM"
        }
        out = ""
        count = 0
        while num > 0:
            digits = 10 ** count
            x = (num % 10) * digits
            if x in mapping:
                out = mapping[x] + out
            elif x / digits > 5:
                x -= 5 * digits
                a = x // digits
                out = mapping[5 * digits] + (a * mapping[digits]) + out
            else:
                a = x // digits
                out = a * mapping[digits] + out
            num = num // 10
            count += 1
        
        return out

