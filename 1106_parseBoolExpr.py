class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operations = []
        conditions = []
        for char in expression:
            if not operations:
                if char == 'f':
                    return False
                if char == 't':
                    return True
            if char in ['!', '|', '&']:
                operations.append((char, len(conditions)))
            elif char in ['t', 'f']:
                conditions.append(True if char == 't' else False)
            elif char == ')':
                operation, index = operations.pop()
                if operation == '!':
                    condition = conditions.pop()
                    if condition:
                        conditions.append(False)
                    else:
                        conditions.append(True)
                elif operation == '&':
                    cut = conditions[index:]
                    conditions = conditions[:index]
                    if all(cut):
                        conditions.append(True)
                    else:
                        conditions.append(False)
                else:
                    cut = conditions[index:]
                    conditions = conditions[:index]
                    if any(cut):
                        conditions.append(True)
                    else:
                        conditions.append(False)
        return conditions[0]
      
# Alternative solution

class Solution1:
    def parseBoolExpr(self, expression: str) -> bool:
        operations = []
        conditions = []
        for char in expression:
            if not operations:
                if char == 'f': return False
                if char == 't': return True
            if char in ['!', '|', '&']:
                operations.append((char, len(conditions)))
            elif char in ['t', 'f']:
                conditions.append(True if char == 't' else False)
            elif char == ')':
                operation, index = operations.pop()
                if operation == '!':
                    conditions[-1] = bool(conditions[-1] ^ True)
                elif operation == '&':
                    conditions = self.operate(conditions, index, all)
                else:
                    conditions = self.operate(conditions, index, any)
        return conditions[0]

    def operate(self, conditions, index, function):
        cut = conditions[index:]
        conditions = conditions[:index]
        if function(cut):
            conditions.append(True)
        else:
            conditions.append(False)
        return conditions
