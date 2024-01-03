class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = 0
        first = second = 0

        for row in bank:
            c = row.count('1')

            if not first:
                first = c
                continue
            
            if not second:
                second = c
                
            if first and second:
                total += first * second
                first, second = second, 0
            
        return total
