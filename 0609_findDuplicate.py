class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for path in paths:
            path_elements = path.split()
            directory = path_elements[0]
            for element in path_elements[1:]:
                i = element.index('(')
                hashmap[element[i+1:-1]].append(directory + '/' + element[:i])
        return [val for val in hashmap.values() if len(val) > 1]
