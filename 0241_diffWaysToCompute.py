class Solution:
    def diffWaysToCompute(self, expression: str, memo: dict = {}) -> List[int]:
        if expression in memo:
            return memo[expression]
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, char in enumerate(expression):
            if char in '*+-':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        memo[expression] = res
        return res
