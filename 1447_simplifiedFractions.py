class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        output = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                if i == 1 or self.GCD(j, i) == 1:
                    output.append(str(i) + "/" + str(j))
        return output

    def GCD(self, a, b):
        if b == 1:
            return 1
        if a % b == 0:
            return b
        return self.GCD(b, a % b)
