class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        pat = self.split(pattern)
        answer = []
        for query in queries:
            que = self.split(query)
            if pat[0][0].isupper():
                if que[0][0].islower():
                    que = que[1:]
            isTrue = True
            if len(pat) != len(que):
                isTrue = False
            else:
                for i in range(0, len(que)):
                    j, k = 0, 0
                    if (que[i][0].isupper() and pat[i][0].islower()) or (que[i][0].islower() and pat[i][0].isupper()):
                        isTrue = False
                        break 
                    if que[i][0].isupper() and pat[i][0].isupper() and que[i][0] != pat[i][0]:
                        isTrue = False
                        break
                    if k != len(pat[i]):
                        while j < len(que[i]):
                            if que[i][j] == pat[i][k]:
                                j += 1
                                k += 1
                                if k == len(pat[i]):
                                    break
                            else:
                                j += 1
                        if k != len(pat[i]):
                            isTrue = False
            answer.append(isTrue)
        return answer
        
    def split(self, pattern):
        splitted_patterns, temp = [], pattern[0]
        for i in range(1, len(pattern)):
            if pattern[i].isupper():
                splitted_patterns.append(temp)
                temp = pattern[i]
            else:
                temp += pattern[i]
        splitted_patterns.append(temp)
        return splitted_patterns
