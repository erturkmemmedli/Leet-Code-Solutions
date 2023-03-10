class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [self.toGrayCode(i) for i in range(2**n)]
    
    def toGrayCode(self, n):
        return n ^ (n >> 1)
