class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
        summ = sum(arr)
        if summ % 3 != 0: return False
        part = summ // 3
        total = 0
        count = 0
        for num in arr:
            total += num
            if total == part:
                count += 1
                total = 0
        return count >= 3
