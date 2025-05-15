class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        output = [(words[0], groups[0])]

        for i in range(1, len(groups)):
            if groups[i] != output[-1][1]:
                output.append((words[i], groups[i]))

        return [w for w, g in output]
