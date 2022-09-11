# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        temp = head
        self.LinkedList = []
        while temp:
            self.LinkedList.append(temp.val)
            temp = temp.next

    def getRandom(self) -> int:
        x = random.randint(0, len(self.LinkedList)-1)
        return self.LinkedList[x]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
