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
    public int max = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return max;
    }

    public int dfs(TreeNode root) {
        if (root.left == null && root.right == null) {
            max = Math.max(max, root.val);
            return Math.max(root.val, 0);
        }

        int left = (root.left != null) ? dfs(root.left) : 0;
        int right = (root.right != null) ? dfs(root.right) : 0;
        max = Math.max(max, left + right + root.val);
        return Math.max(Math.max(left, right) + root.val, 0);
    }
}
