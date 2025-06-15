class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        trgt_a = trgt_b = num_str[0]
        a = b = ""

        if trgt_a == '9':
            for i in range(len(num_str)):
                if num_str[i] != trgt_a:
                    trgt_a = num_str[i]
                    break
        
        if trgt_b == '1':
            for i in range(len(num_str)):
                if num_str[i] > trgt_b:
                    trgt_b = num_str[i]
                    break

        for char in num_str:
            a += '9' if char == trgt_a else char
            b += '0' if char == trgt_b and trgt_b != num_str[0] else '1' if char == trgt_b else char

        return int(a) - int(b)
