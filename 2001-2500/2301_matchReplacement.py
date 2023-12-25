class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        self.char_map = {}

        for key, val in mappings:
            if key not in self.char_map:
                self.char_map[key] = set()
            self.char_map[key].add(val)

        for i in range(len(s) - len(sub) + 1):
            if self.is_equal(s[i:i+len(sub)], sub):
                return True

        return False

    def is_equal(self, target, pattern):
        n = len(target)
        for i in range(n):
            if target[i] == pattern[i] or (pattern[i] in self.char_map and target[i] in self.char_map[pattern[i]]):
                continue
            else:
                return False

        return True
