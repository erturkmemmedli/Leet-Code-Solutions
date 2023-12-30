class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ones = []

        for row in matrix:
            temp = set()

            for i, col in enumerate(row):
                if col == 1:
                    temp.add(i)
                
            ones.append(temp)
        
        d = {}
        result = 0

        for row in ones:
            result = max(result, len(row))

            if not d:
                d = {r:1 for r in row}
                continue

            new_d = {}

            for r in row:
                if r in d:
                    new_d[r] = d[r] + 1
                else:
                    new_d[r] = 1
            
            c = Counter(new_d.values())
            count = 0

            for key, val in sorted([(k, v) for k, v in c.items()], reverse=True):
                count += val
                result = max(result, key * count)

            d = new_d
        
        return result
