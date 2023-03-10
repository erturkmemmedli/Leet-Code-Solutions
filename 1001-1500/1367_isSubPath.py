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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head: return True
        if not root: return False
        return self.dfs(root, head, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, root, head, current):
        #print(root.val if root else "None", head.val if head else "None", current.val if current else "None")
        if not current: return True
        if not root: return False
        if root.val == current.val: current = current.next
        elif root.val == head.val: current = head.next
        else: return False
        if self.dfs(root.left, head, current): return True
        if self.dfs(root.right, head, current): return True
