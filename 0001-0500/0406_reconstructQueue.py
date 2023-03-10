from sortedcontainers import SortedList

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: [x[0], -x[1]])
        indices = SortedList(range(len(people)))
        output = [None] * len(people)
        for height, num in people:
            i = indices[num]
            indices.remove(i)
            output[i] = [height, num]
        return output
