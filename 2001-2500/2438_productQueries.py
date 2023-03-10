class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        binary = bin(n)[2:]
        powers = []
        for i in range(len(binary)-1, -1, -1):
            if binary[i] == '1':
                powers.append(2 ** (len(binary) - i - 1))
        prefix_mult = [1]
        for i in range(len(powers)):
            prefix_mult.append(powers[i] * prefix_mult[-1])
        answer = []
        for a, b in queries:
            answer.append((prefix_mult[b+1] // prefix_mult[a]) % (10**9 + 7))
        return answer
