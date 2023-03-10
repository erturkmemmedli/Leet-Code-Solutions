class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bitMap = []
        for string in arr:
            if len(string) > len(set(string)):
                continue
            self.bitRepresentation(string, bitMap)
        self.max = 0
        self.backtracking(bitMap, 0)
        return self.max

    def bitRepresentation(self, string, bitMap):
        bit = 0
        for char in string:
            bit += 1 << (ord(char) - 97)
        bitMap.append(bit)

    def backtracking(self, bitMap, path):
        if not bitMap:
            self.max = max(self.max, self.onesCount(path))
            return
        for i in range(len(bitMap)):
            if bitMap[i] ^ path == bitMap[i] + path:
                self.backtracking(bitMap[i+1:], path + bitMap[i])
            else:
                self.max = max(self.max, self.onesCount(path))
    
    def onesCount(self, num):
        count = 0
        while num:
            if num % 2 == 1:
                count += 1
            num >>= 1
        return count
