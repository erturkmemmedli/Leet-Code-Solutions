class SegmentTree:
    def __init__(self, xs: list[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, qleft, qright, qval, left, right, pos):
        if self.xs[right + 1] <= qleft or self.xs[left] >= qright: # no overlap
            return
        elif qleft <= self.xs[left] and self.xs[right + 1] <= qright: # full overlap
            self.count[pos] += qval
        else: # partial overlap
            mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos * 2 + 1)
            self.update(qleft, qright, qval, mid + 1, right, pos * 2 + 2)

        if self.count[pos] > 0:
            self.covered[pos] = self.xs[right + 1] - self.xs[left]
        elif left == right:
            self.covered[pos] = 0
        else:
            self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]

    def query(self):
        return self.covered[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs_set = set()
        for x, y, l in squares:
            events.append([y, 1, x, x + l])
            events.append([y + l, -1, x, x + l])
            xs_set.update([x, x + l])
        xs = sorted(xs_set)

        tree = SegmentTree(xs)
        events.sort()

        # First Sweep: calculating total union area
        total_area = 0
        prev_y = events[0][0]
        for y, start, xl, xr in events:
            total_area += tree.query() * (y - prev_y)
            tree.update(xl, xr, start, 0, tree.n - 1, 0)
            prev_y = y

        # Second Sweep: finding minimal y, where area below = half area
        tree = SegmentTree(xs)
        curr_area = 0
        prev_y = events[0][0]
        for y, start, xl, xr in events:
            combined_width = tree.query()
            height_diff = y - prev_y
            area_diff = combined_width * height_diff
            if curr_area + area_diff >= total_area / 2:
                # curr_area + (combined_width * optimal_height_diff) = total_area / 2
                optimal_height_diff = (total_area / 2 - curr_area) / combined_width
                return prev_y + optimal_height_diff
            curr_area += area_diff
            tree.update(xl, xr, start, 0, tree.n - 1, 0)
            prev_y = y
