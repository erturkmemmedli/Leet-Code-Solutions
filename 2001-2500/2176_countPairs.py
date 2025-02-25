class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        val_idx_map = {}
        count = 0

        for i, num in enumerate(nums):
            if num not in val_idx_map:
                val_idx_map[num] = []
            val_idx_map[num].append(i)
        
        for v in val_idx_map.values():
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    if (v[i] * v[j]) % k == 0:
                        count += 1

        return count
