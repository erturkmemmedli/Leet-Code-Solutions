class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []
        for u, t, p in tasks:
            self.task_map[t] = [p, u]
            heappush(self.heap, (-p, -t, u))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = [priority, userId]
        heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_map[taskId][0] = newPriority
        heappush(self.heap, (-newPriority, -taskId, self.task_map[taskId][1]))

    def rmv(self, taskId: int) -> None:
        del self.task_map[taskId]

    def execTop(self) -> int:
        try:
            priority, task, user = heappop(self.heap)
            if -task in self.task_map and [-priority, user] == self.task_map[-task]:
                del self.task_map[-task]
                return user
            else:
                return self.execTop()
        except:
            return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
