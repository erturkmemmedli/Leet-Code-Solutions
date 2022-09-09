class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        permutation = [self.grayCode(n) for n in range(0, 2 ** n)]
        index = permutation.index(start)
        return permutation[index:] + permutation[:index]
        
    def grayCode(self, n):
        return n ^ (n >> 1)
