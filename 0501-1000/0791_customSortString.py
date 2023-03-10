from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        string = Counter(s)
        answer = ""
        for char in order:
            if char in string:
                answer += char * string[char]
                del(string[char])
        for key, val in string.items():
            answer += key * val
        return answer
