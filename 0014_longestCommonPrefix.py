class Solution:
    def longestCommonPrefix(self, strs):
        output = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(strs[i]) and j < len(output):
                if output[j] == strs[i][j]:
                    j += 1
                else:
                    break
            output = output[:j]
        return output
