class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        total = 0
        i, j = 0, 1

        while j < len(colors):
            if colors[j] != colors[j - 1]:
                if j - i + 1 >= k:
                    total += 1
                j += 1
            else:
                i = j
                j += 1

        return total
