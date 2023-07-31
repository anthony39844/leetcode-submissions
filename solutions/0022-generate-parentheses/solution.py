class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses_list = []
        s = ""
        def generate(s, open_parentheses, close_parentheses):
            if len(s) == 2 * n:
                parentheses_list.append(s)
                return
            if open_parentheses < n:
                generate(s + '(', open_parentheses + 1, close_parentheses)
            if close_parentheses < open_parentheses:
                generate(s + ')', open_parentheses, close_parentheses + 1)

        generate(s, 0, 0)
        return parentheses_list



        
