class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress = []
        for i in range(0, len(nums), 2):
            decompress += [nums[i+1]] * nums[i]
        return decompress
      
# Alternative solution

class Solution1:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress = []
        for i in range(0, len(nums), 2):
            for _ in range(nums[i]):
                decompress.append(nums[i+1])
        return decompress
