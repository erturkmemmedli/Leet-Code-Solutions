class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        counter = collections.Counter(nums)
        queue = collections.deque()
        for num in sorted(counter):
            if not queue or queue[-1] + 1 == num and len(queue) < k:
                queue.append(num)
            elif queue[-1] + 1 < num:
                return False
            if len(queue) == k:
                pop = queue.popleft()
                cnt = counter[pop]
                for i in queue:
                    counter[i] -= cnt
                    if counter[i] < 0:
                        return False
                while queue:
                    if counter[queue[0]] == 0:
                        queue.popleft()
                    else:
                        break
        return True if not queue else False 
