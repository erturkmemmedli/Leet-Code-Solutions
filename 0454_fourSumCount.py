from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        a = self.twoSumCount(nums1, nums2)
        b = self.twoSumCount(nums3, nums4)
        result = 0
        for num in a:
            if -num in b:
                result += a[num] * b[-num]
        return result        
        
    def twoSumCount(self, nums1, nums2):
        hashmap = defaultdict(int)
        for x in nums1:
            for y in nums2:
                hashmap[x + y] += 1
        return hashmap

# Alternative solution (which gives TLE error)

from collections import defaultdict

class Solution1:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}
        for num in nums1:
            if num not in hashmap:
                hashmap[num] = [self.threeSumCount(nums2, nums3, nums4, -num), 1]
            else:
                hashmap[num][1] += 1
        return sum([v[0] * v[1] for v in hashmap.values()])
            
    def threeSumCount(self, nums1, nums2, nums3, target):
        hashmap = {}
        for num in nums1:
            if num not in hashmap:
                hashmap[num] = [self.twoSumCount(nums2, nums3, target - num), 1]
            else:
                hashmap[num][1] += 1
        return sum([v[0] * v[1] for v in hashmap.values()])
            
    def twoSumCount(self, nums1, nums2, target):
        hashmap = defaultdict(int)
        result = 0
        for num in nums1:
            hashmap[target - num] += 1
        for num in nums2:
            if num in hashmap:
                result += hashmap[num]
        return result

# Alternative solution (which gives TLE error)

from collections import defaultdict

class Solution2:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        self.output = 0
        for num in nums1:
            self.threeSumCount(nums2, nums3, nums4, -num)
        return self.output
            
    def threeSumCount(self, nums1, nums2, nums3, target):
        for num in nums1:
            self.twoSumCount(nums2, nums3, target - num)
            
    def twoSumCount(self, nums1, nums2, target):
        hashmap = defaultdict(int)
        for num in nums1:
            hashmap[target - num] += 1
        for num in nums2:
            if num in hashmap:
                self.output += hashmap[num]
