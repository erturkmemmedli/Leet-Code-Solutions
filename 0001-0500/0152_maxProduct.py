class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = 0
        firstNegativeIndex = None
        product = False
        maxProduct = -float('inf')
        while i < len(nums):
            if nums[i] == 0:
                maxProduct = max(maxProduct, 0)
                firstNegativeIndex = None
                product = False
            elif not product:
                maxProduct = max(maxProduct, nums[i])
                if nums[i] < 0:
                    firstNegativeIndex = i
                product = True
            else:
                if firstNegativeIndex == None and nums[i] < 0:
                    firstNegativeIndex = i
                nums[i] *= nums[i-1]
                if nums[i] > 0:
                    maxProduct = max(maxProduct, nums[i])
                else:
                    maxProduct = max(maxProduct, nums[i] // nums[firstNegativeIndex])
            i += 1
        return maxProduct
