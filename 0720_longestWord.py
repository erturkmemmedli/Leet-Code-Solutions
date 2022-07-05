class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = len)
        s = set("")
        out = "~"
        for word in words:
            if len(word) == 1:
                s.add(word)
                out = min(out, word)
            else:
                if word[:-1] in s:
                    s.add(word)
        for word in words:
            if word[:-1] in s:
                if len(word) == len(out):
                    out = min(out, word)
                else:
                    out = word
        return out if out != '~' else ""
