class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[j]) < len(words[i]):
                    if words[j] in words[i]:
                        output.add(words[j])
                else:
                    if words[i] in words[j]:
                        output.add(words[i])
        return output
