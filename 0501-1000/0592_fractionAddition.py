class Solution:
    def fractionAddition(self, expression: str) -> str:
        curr = expression[0]
        a, b = 0, 1
        pos = 1

        for i in range(1, len(expression)):
            if expression[i] not in '-+':
                curr += expression[i]
                continue

            split_div = curr.split('/')

            if len(split_div) == 1:
                c = split_div[0]
                a += b * (int(c) if pos else -int(c))
            else:
                c, d = split_div
                a = a * int(d) + b * (int(c) if pos else -int(c))
                b *= int(d)

            a, b = self.find_irreducable_fraction(a, b)
            curr = ""
            pos = int(expression[i] == '+')

        split_div = curr.split('/')
        if len(split_div) == 1:
            c = split_div[0]
            a += b * (int(c) if pos else -int(c))
        else:
            c, d = split_div
            a = a * int(d) + b * (int(c) if pos else -int(c))            
            b *= int(d)

        a, b = self.find_irreducable_fraction(a, b)
        return f'{a}/{b}'
                
    def find_irreducable_fraction(self, a, b):
        gcd = self.gcd(a, b)
        return a//gcd, b//gcd
    
    def gcd(self, a, b):
        while a % b != 0:
            a, b = b, a % b
        return b
