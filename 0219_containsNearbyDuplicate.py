class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = {}
        for ind, num in enumerate(nums):
            if num not in D:
                D[num] = [ind]
            else:
                D[num].append(ind)
        for v in D.values():
            if len(v) == 1:
                continue
            for i in range(len(v)):
                for j in range(i+1, len(v)):
                    if v[j] - v[i] <= k:
                        return True
        return False
