class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for person, size in enumerate(groupSizes):
            if size not in d:
                d[size] = [person]
            else:
                d[size].append(person)
        output = []
        for k, v in d.items():
            for i in range(0, len(v), k):
                output.append(v[i:i+k])
        return output
      
# Alternative solution

class Solution1:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        output = []
        for person, size in enumerate(groupSizes):
            if size not in d:
                d[size] = [person]
            else:
                d[size].append(person)
            if len(d[size]) == size:
                output.append(d[size])
                d[size] = []
        return output
