class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap = {}
        for num in arr:
            if num - difference in hashmap:
                hashmap[num] = hashmap[num - difference] + 1
            else:
                hashmap[num] = 1
        return max(hashmap.values())
