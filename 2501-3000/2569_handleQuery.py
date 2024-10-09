class SegmentTree:
    def __init__(self, arr: List[int]):
        """Build segment tree."""
        self.n = n = len(arr)
        self.tree = [0]*4*n
        self.lazy = [0]*4*n
        
        def build(i: int, low: int, high: int) -> None: 
            """Build segment tree from array."""
            if low + 1 == high:
                self.tree[i] = arr[low]
            else: 
                mid = low + high >> 1
                build(2*i+1, low, mid)
                build(2*i+2, mid, high)
                self.tree[i] = self.tree[2*i+1] + self.tree[2*i+2]
        
        build(0, 0, n)

    def update(self, qlow: int, qhigh: int, i: int = 0, low: int = 0, high: int = 0) -> None:
        """Update segment tree when value in [qlow, qhigh) is flipped."""
        if not high: 
            high = self.n

        if self.lazy[i]: 
            self.tree[i] = (high - low) - self.tree[i]

            if low + 1 < high: 
                self.lazy[2*i+1] ^= 1
                self.lazy[2*i+2] ^= 1 

            self.lazy[i] = 0

        if low < high and qlow < high and low < qhigh: 
            if qlow <= low and high <= qhigh: # total overlap
                self.tree[i] = (high - low) - self.tree[i]

                if low + 1 < high: 
                    self.lazy[2*i+1] ^= 1
                    self.lazy[2*i+2] ^= 1

                return 

            mid = low + high >> 1
            self.update(qlow, qhigh, 2*i+1, low, mid) 
            self.update(qlow, qhigh, 2*i+2, mid, high)
            self.tree[i] = self.tree[2*i+1] + self.tree[2*i+2]


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(nums1)
        answer = []
        val = sum(nums2)

        for x, y, z in queries: 
            if x == 1: 
                tree.update(y, z+1)
            elif x == 2: 
                val += y * tree.tree[0]
            else: 
                answer.append(val)

        return answer
