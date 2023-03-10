class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for num in nums:
            if num:
                product *= num
            else:
                count += 1
        if count > 1:
            return [0] * len(nums)
        elif count == 1:
            return [0 if num else product for num in nums]
        elif count == 0:
            return [product // nums[i] for i in range(len(nums))]
           
# Alternative solution

class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
            result[-1-i] *= suffix
            suffix *= nums[-1-i]
        return result
