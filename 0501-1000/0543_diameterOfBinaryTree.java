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
    public int diameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return diameter;
    }

    public int dfs(TreeNode root) {
        if (root.left == null && root.right == null) {
            return 0;
        }

        int left = (root.left != null) ? dfs(root.left) + 1 : 0;
        int right = (root.right != null) ? dfs(root.right) + 1 : 0;
        diameter = Math.max(diameter, left + right);
        return Math.max(left, right);
    }
}
