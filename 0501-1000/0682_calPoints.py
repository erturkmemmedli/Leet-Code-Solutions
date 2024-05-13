class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            match op:
                case '+':
                    record.append(record[-1] + record[-2])
                case 'D':
                    record.append(record[-1] * 2)
                case 'C':
                    record.pop()
                case _:
                    record.append(int(op))

        return sum(record)
