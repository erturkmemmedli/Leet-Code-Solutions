class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = [0]

        for num in arr:
            prefix.append(prefix[-1] + num)

        res = 0
        i = 1

        while i < len(prefix):
            for j in range(i, len(prefix)):
                res += prefix[j] - prefix[j - i]
            
            i += 2
        
        return res
