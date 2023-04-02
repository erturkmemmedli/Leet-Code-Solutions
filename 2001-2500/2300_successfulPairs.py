class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []

        for spell in spells:
            pairs.append(len(potions) - self.binary_search(potions, spell, success, 0, len(potions)))

        return pairs

    def binary_search(self, potions, spell, target, left, right):
        while left < right:
            mid = left + (right - left) // 2

            if potions[mid] * spell >= target:
                right = mid
            else:
                left = mid + 1

        return left
