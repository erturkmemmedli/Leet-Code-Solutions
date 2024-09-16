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
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> output = new ArrayList<>();
        if (root == null) return output;
        List<Integer> path = new ArrayList<>(Arrays.asList(root.val));
        dfs(root, targetSum, output, path);
        return output;
    }

    public void dfs(TreeNode root, int targetSum, List<List<Integer>> output, List<Integer> path) {
        if (root.left == null && root.right == null && targetSum - root.val == 0) {
            output.add(new ArrayList<Integer>(path));
            return;
        }

        if (root.left != null) {
            path.add(root.left.val);
            dfs(root.left, targetSum - root.val, output, path);
            path.remove(path.size() - 1);
        }
        if (root.right != null) {
            path.add(root.right.val);
            dfs(root.right, targetSum - root.val, output, path);
            path.remove(path.size() - 1);
        }
    }
}
