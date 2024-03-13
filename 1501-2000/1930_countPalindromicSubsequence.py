class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_last_index_map = {}
        output = 0

        for i, char in enumerate(s):
            if char not in first_last_index_map:
                first_last_index_map[char] = [i, None]
            else:
                first_last_index_map[char][1] = i
            
        for start, end in first_last_index_map.values():
            if end != None:
                output += len(set(s[start+1:end]))

        return output
