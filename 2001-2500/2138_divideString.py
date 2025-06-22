class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        m = len(s) % k
        s += (fill * (k - m)) if m != 0 else ""
        return [s[i:i+k] for i in range(0, len(s), k)]
