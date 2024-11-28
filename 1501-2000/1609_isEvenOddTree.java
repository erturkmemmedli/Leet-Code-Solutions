/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        boolean isEvenLevel = true;
        queue.add(root);

        while (!queue.isEmpty()) {
            int length = queue.size();
            int lastNodeVal = (isEvenLevel) ? Integer.MIN_VALUE : Integer.MAX_VALUE;

            for (int i = 0; i < length; i++) {
                TreeNode node = queue.poll();

                if ((isEvenLevel && node.val % 2 == 0) || (!isEvenLevel && node.val % 2 != 0)) {
                    return false;
                }

                if ((isEvenLevel && node.val <= lastNodeVal) || (!isEvenLevel && node.val >= lastNodeVal)) {
                    return false;
                }

                lastNodeVal = node.val;

                if (node.left != null) {
                    queue.add(node.left);
                }

                if (node.right != null) {
                    queue.add(node.right);
                }
            }
            
            isEvenLevel ^= true;
        }

        return true;
    }
}
