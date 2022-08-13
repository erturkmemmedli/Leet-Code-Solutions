class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, number in enumerate(numbers):
            if number not in hashmap:
                hashmap[target-number] = i + 1
            else:
                return [hashmap[number], i + 1]
