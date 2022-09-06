"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hashmap = {}
        for employee in employees:
            hashmap[employee.id] = (employee.importance, employee.subordinates)
        return self.bfs(hashmap, id)
        
    def bfs(self, hashmap, id):
        total = 0
        queue = deque([id])
        while queue:
            employee = queue.popleft()
            total += hashmap[employee][0]
            queue += hashmap[employee][1]
        return total
