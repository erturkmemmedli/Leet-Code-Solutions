class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return
        c = Counter()
        for i in range(len(s) - 9):
            c[s[i:i+10]] += 1
        answer = []
        for key, val in c.items():
            if val > 1:
                answer.append(key)
        return answer
