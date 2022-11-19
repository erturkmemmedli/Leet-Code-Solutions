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

# Alternative solution

class Solution1:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashset = set(list1) & set(list2)
        index = []
        for item in hashset:
            index.append((item, list1.index(item) + list2.index(item)))
        index = sorted(index, key = lambda x: x[1])
        i = 0
        while i < len(index):
            if index[i][1] == index[0][1]:
                i += 1
                continue
            break
        return [index[j][0] for j in range(i)]
    
# Alternative solution

class Solution2:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary = {k:v for v, k in enumerate(list1)}
        result = []
        temp = float('inf')
        for v, k in enumerate(list2):
            minimum = dictionary.get(k, float('inf'))
            if minimum + v < temp:
                temp = minimum + v
                result = [k]
            elif minimum + v == temp:
                result.append(k)
        return result
