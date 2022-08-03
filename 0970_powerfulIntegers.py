class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_pow = [1]
        i = 1
        while x ** i < bound and x != 1:
            x_pow.append(x ** i)
            i += 1
        y_pow = [1]
        i = 1
        while y ** i < bound and y != 1:
            y_pow.append(y ** i)
            i += 1
        output = set()
        for i in x_pow:
            for j in y_pow:
                if i + j <= bound:
                    output.add(i+j)
                else:
                    break
        return output
