class SegmentTree:
    def __init__(self, xs):
        self.cnts = collections.defaultdict(int)
        self.total = collections.defaultdict(int)
        self.xs = xs

    def update(self, v, tl, tr, l, r, h):
        if l > r:
            return

        if l == tl and r == tr:
            self.cnts[v] += h
        else:
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), h)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, h)

        if self.cnts[v] > 0:
            self.total[v] = self.xs[tr+1] - self.xs[tl]
        else:
            self.total[v] = self.total[v*2] + self.total[v*2+1]

        return self.total[v]

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1,x2]]))
        xs_i = {v:i for i, v in enumerate(xs)}
        Tree = SegmentTree(xs)

        List = []
        for x1, y1, x2, y2 in rectangles:
            List.append([y1, 1, x1, x2])
            List.append([y2, -1, x1, x2])
        List.sort()

        curr_y, curr_x_sum, area = 0, 0, 0
        for y, op_cl, x1, x2 in List:
            area += (y - curr_y) * curr_x_sum
            curr_y = y
            Tree.update(1, 0, len(xs) - 1, xs_i[x1], xs_i[x2] - 1, op_cl)
            curr_x_sum = Tree.total[1]
            
        return area % (10 ** 9 + 7)
