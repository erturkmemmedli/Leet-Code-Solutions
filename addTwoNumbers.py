class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):

    def __init__(self):
        self.remainder = 0
		
    def addTwoNumbers(self, l1, l2):
        if l1 is not None and l2 is not None:
            node = ListNode()
            node.val = (l1.val + l2.val + self.remainder) % 10
            self.remainder = (l1.val + l2.val + self.remainder) // 10
            node.next = self.addTwoNumbers(l1.next, l2.next)
            return node
        elif l1 is not None and l2 is None:
            node = ListNode()
            node.val = (l1.val + self.remainder) % 10
            self.remainder = (l1.val + self.remainder) // 10
            l2 = ListNode() 
            node.next = self.addTwoNumbers(l1.next, l2.next)
            return node
        elif l1 is None and l2 is not None:
            node = ListNode() 
            node.val = (l2.val + self.remainder) % 10
            self.remainder = (l2.val + self.remainder) // 10 
            l1 = ListNode()
            node.next = self.addTwoNumbers(l1.next, l2.next)
            return node
        else:
            if self.remainder == 1:
                node = ListNode()
                node.val = 1
                return node	
            return
