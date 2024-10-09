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

# Alternative solution (TLE)

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        

class SegmentTree:
    def __init__(self, nums: List[int]):
        def build(nums, l, r):
            if l > r:
                return None
                
            if l == r:
                n = SegmentTreeNode(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2
            root = SegmentTreeNode(l, r)
            root.left = build(nums, l, mid)
            root.right = build(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
            return root
        
        self.root = build(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            
            root.total = root.left.total + root.right.total
            return root.total
        
        return updateVal(self.root, index, val)

    def sum(self, left: int, right: int) -> int:
        def rangeSum(root, i, j):            
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2

            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)
        
        return rangeSum(self.root, left, right)


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(nums1)
        answer = []
        val = sum(nums2)

        for x, y, z in queries: 
            if x == 1: 
                for i in range(y, z + 1):
                    nums1[i] ^= 1
                    tree.update(i, nums1[i])
            elif x == 2: 
                val += y * tree.root.total
            else: 
                answer.append(val)

        return answer
