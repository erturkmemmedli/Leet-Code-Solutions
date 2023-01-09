class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        array = []
        for num in nums:
            array.append(nums[num])
        return array
