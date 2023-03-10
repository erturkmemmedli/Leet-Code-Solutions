class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_copy = [''.join(sorted(s)) for s in strs]
        d = {}
        for i, s in enumerate(sorted_copy):
            if s not in d:
                d[s] = [strs[i]]
            else:
                d[s].append(strs[i])
        return d.values()
