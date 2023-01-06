class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        dictionary = {}
        width = valueDiff + 1
        for i, num in enumerate(nums):
            val = num // width
            if val in dictionary:
                return True
            if val - 1 in dictionary and abs(num - dictionary[val - 1]) < width:
                return True
            if val + 1 in dictionary and abs(num - dictionary[val + 1]) < width:
                return True
            dictionary[val] = num
            if i >= indexDiff:
                del dictionary[nums[i - indexDiff] // width]
