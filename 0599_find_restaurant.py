class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        for i, s in enumerate(list1):
            d1[s] = i
        d2 = {}
        for i, s in enumerate(list2):
            if s in d1:
                d2[s] = d1[s] + i
        m = min(d2.values())
        result = []
        for k,v in d2.items():
            if v == m: result.append(k)
        return result
