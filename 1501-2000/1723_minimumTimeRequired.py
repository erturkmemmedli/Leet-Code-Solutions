class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.work_done = [0] * k
        self.minimum_work = float("inf")
        self.dfs(jobs, 0, k)
        return self.minimum_work

    def dfs(self, jobs, index, k):
        if index == len(jobs):
            self.minimum_work = min(self.minimum_work, max(self.work_done))
            return
        visited = set()
        for i in range(k):
            if self.work_done[i] in visited:
                continue
            if self.work_done[i] + jobs[index] >= self.minimum_work:
                continue
            visited.add(self.work_done[i])
            self.work_done[i] += jobs[index]
            self.dfs(jobs, index + 1, k)
            self.work_done[i] -= jobs[index]

# Alternative solution (which gives TLE error)

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        subsets = deque([[]])
        memo = set()

        for i in range(len(jobs)):
            for _ in range(len(subsets)):
                subset = subsets.popleft()
                if len(jobs) - i - 1 + len(subset) >= k:
                    for j in range(len(subset)):
                        new_subset = subset[:]
                        new_subset[j] += jobs[i]
                        tupled = tuple(sorted(new_subset))
                        if tupled not in memo:
                            subsets.append(new_subset)
                            memo.add(tupled)
                        
                if len(subset) < k:
                    new_subset = subset[:]
                    new_subset.append(jobs[i])
                    tupled = tuple(sorted(new_subset))
                    if tupled not in memo:
                        subsets.append(new_subset)
                        memo.add(tupled)  

        time = float("inf")
        for subset in subsets:
            if len(subset) == k:
                time = min(time, max(subset))
        return time
