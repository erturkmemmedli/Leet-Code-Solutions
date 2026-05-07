class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        curr = set()
        output = []

        for num in nums:
            curr.add(num)
            counter[num] -= 1
            if not counter[num]:
                del counter[num]
            output.append(len(curr) - len(counter))

        return output
