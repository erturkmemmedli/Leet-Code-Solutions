class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        commands = []
        idx_map = {}
        curr_idx = None
        curr_val = 0

        for s, e in queries:
            commands.append([s, 0])
            commands.append([e + 1, 1])

        commands.sort()

        for idx, state in commands:
            idx_map[idx] = idx_map.get(idx, 0) + (1 if state == 0 else -1)
        
        for i, num in enumerate(nums):
            if i in idx_map:
                curr_idx = i
                curr_val += idx_map[i]
            
            if curr_val < num:
                return False
        
        return True
