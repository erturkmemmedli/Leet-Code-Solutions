class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        result = ""
        prev = 0
        for idx, src, trgt in sorted(zip(indices, sources, targets)):
            if s[idx:idx+len(src)] == src:
                result += s[prev:idx]
                result += trgt
                prev = idx + len(src)
        if prev < len(s):
            result += s[prev:]
        return result
