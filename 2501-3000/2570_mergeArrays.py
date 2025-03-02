class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        for id, val in nums1:
            hashmap[id] = val

        for id, val in nums2:
            hashmap[id] = hashmap.get(id, 0) + val

        return sorted([k, v] for k, v in hashmap.items())
