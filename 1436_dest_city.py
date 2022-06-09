class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = set()
        for start, end in paths:
            d.add(start)
        for start, end in paths:
            if end not in d:
                return end
