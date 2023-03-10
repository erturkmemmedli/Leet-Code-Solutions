# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        array = []
        temp = head
        while temp:
            array.append(temp.val)
            temp = temp.next
        return self.divide_and_conquer(array)
        
    def divide_and_conquer(self, array):
        if len(array) == 0:
            return
        if len(array) == 1:
            return TreeNode(array[0])
        m = len(array) // 2
        root = TreeNode(array[m])
        root.left = self.divide_and_conquer(array[:m])
        root.right = self.divide_and_conquer(array[m+1:])
        return root

# Alternative solution

class Solution1:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return
        return self.div_and_con(head, None)
        
    def div_and_con(self, start, end):
        if start == end:
            return
        if start.next == end:
            return TreeNode(start.val)
        fast, slow = start, start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val, self.div_and_con(start, slow), self.div_and_con(slow.next, end))
        return root
