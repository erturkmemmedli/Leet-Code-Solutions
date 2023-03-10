class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < n:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                dic = stack.pop()
                i += 1
                repeat = ""
                while i < n and formula[i].isdigit():
                    repeat += formula[i]
                    i += 1
                for key, val in dic.items():
                    stack[-1][key] += val * (int(repeat) if repeat else 1)
            else:
                element = formula[i]
                i += 1
                while i < n and formula[i].islower():
                    element += formula[i]
                    i += 1
                atom = ""
                while i < n and formula[i].isdigit():
                    atom += formula[i]
                    i += 1
                stack[-1][element] += int(atom) if atom else 1
        return "".join([key + (str(val) if val > 1 else "") for key, val in sorted(stack[-1].items())])
