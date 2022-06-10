class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = []
        for i, ch in enumerate(s):
            if ch == c: indices.append(i)
        result = []
        index = 0
        for i in range(len(s)):
            if i > indices[index]:
                if index < len(indices) - 1:
                    index += 1
            if index == 0:
                result.append(abs(i - indices[index]))
            else:
                result.append(min(abs(i - indices[index]), abs(i - indices[index-1])))
        return result
