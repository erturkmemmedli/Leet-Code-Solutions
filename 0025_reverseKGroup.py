# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.count = 0
        self.output = []
        self.stack = []
        self.node = None
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.recursive(head, k)
        self.output.append(None)
        for i in range(len(self.output)-1):
            self.output[i].next = self.output[i+1]
        return self.output[0]
        
    def recursive(self, head, k):
        if self.count == k:
            self.stack = self.stack[::-1]
            self.output += self.stack
            self.count = 0
            self.stack = []
        if head is None:
            self.output += self.stack
            return
        self.stack.append(head)
        self.count += 1
        self.recursive(head.next, k)
        return

# Alternative solution

class Solution1:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = node = ListNode(-1)
        dummy.next = left = right = head
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count == k:
                prev, curr = right, left
                for _ in range(k):
                    curr.next, curr, prev = prev, curr.next, curr
                node.next, node, left = prev, left, right
            else:
                return dummy.next

# Alternative solution

class Solution2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        cur, count = head, 0
        while cur:
            cur = cur.next
            count += 1
        if count < k:
            return head
        dummy = pre = ListNode(-1)
        dummy.next = head
        for i in range(count // k):
            prev = None
            for j in range(k - 1):
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            temp = head.next
            head.next = prev
            pre.next.next = temp
            node = pre.next
            pre.next = head
            head = temp
            pre = node
        return dummy.next

# Alternative solution

class Solution3:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
        curr = head
        prev = None
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head.next = self.reverseKGroup(curr, k)
        return prev

# Alternative solution

class Solution4:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        length = self.findLength(head)
        reverseCount = length // k
        temp, finalHead, finalTail = head, None, None
        while reverseCount:
            reverseCount -= 1
            newHead, newTail, newNext = self.determineHeadAndTail(temp, k)
            if not finalHead:
                finalHead = newHead
            if not finalTail:
                finalTail = newTail
            else:
                finalTail.next = newHead
                finalTail = newTail
            temp = newNext
        finalTail.next = newNext
        return finalHead

    def findLength(self, node):
        temp, length = node, 0
        while temp:
            temp, length = temp.next, length + 1
        return length

    def determineHeadAndTail(self, node, k):
        prev, curr = None, node
        while k:
            k -= 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev, node, curr
