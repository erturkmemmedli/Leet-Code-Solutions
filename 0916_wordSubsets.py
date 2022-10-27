class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b = collections.Counter()
        for word in words2:
            c = collections.Counter(word)
            for k, v in c.items():
                if k in b:
                    b[k] = max(b[k], v)
                else:
                    b[k] = v
        output = []
        for word in words1:
            c = collections.Counter(word)
            if not b - c:
                output.append(word)
        return output
