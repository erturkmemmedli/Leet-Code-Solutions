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
