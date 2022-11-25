class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack, result, current = [], [], []
        for char in expression:
            if char == '{':
                stack.append(result)
                stack.append(current)
                result, current = [], []
            elif char.islower():
                current = [i + char for i in (current or [''])]
            elif char == ',':
                result += current
                current = []
            elif char == '}':
                preCurrent, preResult = stack.pop(), stack.pop()
                current = [x + y for y in (result + current) for x in (preCurrent or [''])]
                result = preResult
        return sorted(set(result+current))
