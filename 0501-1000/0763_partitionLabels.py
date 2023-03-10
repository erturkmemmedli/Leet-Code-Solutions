class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chars = dict()
        for index, char in enumerate(s):
            if char not in chars:
                chars[char] = [index]
            else:
                chars[char].append(index)
        out = []
        start = chars[s[0]][0]
        end = chars[s[0]][-1]
        for i in range(1, len(s)):
            if chars[s[i]][0] < end:
                end = max(end, chars[s[i]][-1])
            else:
                out.append(end - start + 1)
                start = chars[s[i]][0]
                end = chars[s[i]][-1]
        out.append(end - start + 1)
        return out
