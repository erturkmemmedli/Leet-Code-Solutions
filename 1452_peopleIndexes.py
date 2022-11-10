class Solution:
    def __init__(self):
        self.prime = 263
        self.multiplyer = 1000000007

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        hashmap = [set() for _ in range(n)]
        for i in range(n):
            for j in range(len(favoriteCompanies[i])):
                hashmap[i].add(self.hashFunction(favoriteCompanies[i][j]))
        result = []
        for i in range(n):
            isSubset = False
            for j in range(n):
                if i != j:
                    if len(hashmap[i] - hashmap[j]) == 0:
                        isSubset = True
                        break
            if not isSubset:
                result.append(i)
        return result

    def hashFunction(self, string):
        hashValue = 0
        for i in range(len(string)):
            hashValue = (hashValue + ord(string[i]) * (self.prime ** i)) % self.multiplyer
        return hashValue
