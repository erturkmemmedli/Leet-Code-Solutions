class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        decomposition = ""
        primitive = ""
        stack = []
        for parantheses in s:
            if not stack:
                stack.append(parantheses)
                primitive += parantheses
                continue
            elif parantheses == '(':
                stack.append(parantheses)
                primitive += parantheses
            elif parantheses == ')':
                primitive += parantheses
                stack.pop()
                if not stack:
                    decomposition += primitive[1:len(primitive)-1]
                    primitive = ""
        return decomposition
