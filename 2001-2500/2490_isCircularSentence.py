class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        for i in range(len(s)):
            if s[i][0] != s[i-1][-1]:
                return False
            
        return True
