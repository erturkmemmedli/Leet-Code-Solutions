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

# Alternative solution

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        count = 0
        for char in s:
            if char == '(':
                stack += 1
            elif stack:
                stack -= 1
            else:
                count += 1
        count += stack
        return count
