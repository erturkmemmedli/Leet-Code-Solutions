class Solution:
    def __init__(self):
        self.r1 = set("qwertyuiop")
        self.r2 = set("asdfghjkl")
        self.r3 = set("zxcvbnm")
        
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        for word in words:
            w = word.lower()
            if w[0] in self.r1:
                r = self.r1
            elif w[0] in self.r2:
                r = self.r2
            elif w[0] in self.r3:
                r = self.r3
            w = set(w)
            if len(r) - len(w) == len(r - w):
                output.append(word)
        return output
