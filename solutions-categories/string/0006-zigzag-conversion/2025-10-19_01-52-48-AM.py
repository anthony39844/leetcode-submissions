class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        pattern = (numRows - 1) * 2
        out = ""
        row = 0
        while row < numRows:
            index = row
            while index < len(s):
                out += s[index]
                if row != 0 and row != numRows - 1 and index + pattern - (row * 2) < len(s):
                    out += s[index + pattern - (row * 2)]
                index += pattern

            row += 1

        return out
            

