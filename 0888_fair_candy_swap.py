class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        mid = (alice + bob) // 2
        target = abs(alice - mid)
        sett = set(aliceSizes)
        for num in bobSizes:
            if mid - bob + num in sett:
                return [mid - bob + num, num]
