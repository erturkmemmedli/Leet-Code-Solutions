# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        index = self.findPeakInMountainArray(mountain_arr)
        if mountain_arr.get(index) == target:
            return index
        idx = self.binarySearch(target, mountain_arr, 0, index - 1, False)
        return idx if idx != -1 else self.binarySearch(target, mountain_arr, index + 1, mountain_arr.length() - 1, True)
        
    def findPeakInMountainArray(self, mountain_arr):
        length = mountain_arr.length()
        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid + 1) > mountain_arr.get(mid):
                left = mid + 1
            else:
                right = mid
        return left
        
    def binarySearch(self, target, mountain_arr, left, right, reverse):
        while left <= right:
            mid = left + (right - left) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif (not reverse and val > target) or (reverse and val < target):
                right = mid - 1
            else:
                left = mid + 1
        return -1
