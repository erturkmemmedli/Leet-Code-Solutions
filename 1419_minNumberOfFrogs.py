class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogMap = collections.defaultdict(list)
        for i in range(len(croakOfFrogs)-1, -1, -1):
            frogMap[croakOfFrogs[i]].append(i)
        length = len(frogMap['c'])
        for val in frogMap.values():
            if len(val) != length:
                return -1
        croak = []
        while frogMap['c']:
            c = frogMap['c'].pop()
            r = frogMap['r'].pop()
            o = frogMap['o'].pop()
            a = frogMap['a'].pop()
            k = frogMap['k'].pop()
            if not (c < r < o < a < k):
                return -1
            else:
                croak.append((c, k))
        frogs = collections.deque()
        for start, end in croak:
            if frogs and start > frogs[0][1]:
                frogs.popleft()
            frogs.append((start, end))
        return len(frogs)
