from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        array = []
        for num in nums1:
            hashmap[num].append(num)
        for num in nums2:
            if num in hashmap:
                array.append(hashmap[num].pop())
                if not hashmap[num]:
                    del(hashmap[num])
        return array
