# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.count = 0
        self.length = 1
        self.flag = False
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if self.count == 0:
            if head.next is None:
                self.count += 1
                return None
            else:
                self.length += 1
                self.removeNthFromEnd(head.next, n)              
        if self.length == n: return head.next                
        if self.count == n: self.flag = True        
        self.count += 1  
        if self.flag == True:
            head.next = head.next.next
            self.flag = False
        return head

# Alternative solution

class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        current = head
        deleted = head
        c = 1
        while current:
            current = current.next
            if current:
                if c == n:
                    prev = deleted
                    deleted = deleted.next
                if c < n:
                    c += 1
            else:
                if prev.next == head:
                    head = head.next
                prev.next = deleted.next
        return head
