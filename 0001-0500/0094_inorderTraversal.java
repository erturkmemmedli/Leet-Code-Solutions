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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inorderTree = new ArrayList<>();
        dfs(root, inorderTree);
        return inorderTree;
    }

    public void dfs(TreeNode root, List<Integer> tree) {
        if (root == null) {
            return;
        }

        dfs(root.left, tree);
        tree.add(root.val);
        dfs(root.right, tree);
    }
}
