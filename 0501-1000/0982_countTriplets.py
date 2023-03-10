class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        bitNums = []
        maxLength = 0
        for num in nums:
            bitNums.append(bin(num)[2:])
            maxLength = max(maxLength, len(bitNums[-1]))
        for i in range(len(nums)):
            frontZeros = maxLength - len(bitNums[i])
            bitNums[i] = '0' * frontZeros + bitNums[i]
        row, col = len(bitNums), len(bitNums[0])
        ones = collections.defaultdict(set)
        for i in range(row):
            for j in range(col):
                if bitNums[i][j] == '1':
                    ones[j].add(i)
        VennDiagram = collections.defaultdict(list)
        count = 0
        for j in range(col):
            if len(ones[j]) != 0:
                count += len(ones[j]) ** 3
                for i in range(j, 0, -1):
                    for previous in VennDiagram[i]:
                        intersection = previous & ones[j]
                        if len(intersection) != 0:
                            count += (-1) ** i * len(intersection) ** 3
                            VennDiagram[i + 1].append(intersection)
                VennDiagram[1].append(ones[j])
        return len(nums) ** 3 - count
