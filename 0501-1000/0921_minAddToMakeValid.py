class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        moves = 0
        for parantez in s:
            if parantez == '(':
                stack.append('(')
            if parantez == ')':
                if stack:
                    stack.pop()
                else:
                    moves += 1
        moves += len(stack)
        return moves
