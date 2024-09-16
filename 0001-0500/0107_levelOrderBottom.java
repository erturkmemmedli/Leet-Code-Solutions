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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> output = new ArrayList<>();
        Stack<List<Integer>> stack = new Stack<>();

        if (root == null) return output;

        Queue<TreeNode> queue = new LinkedList<>(){{add(root);}};

        while (!queue.isEmpty()) {
            int length = queue.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < length; i++) {
                TreeNode node = queue.remove();
                level.add(node.val);

                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            
            stack.push(level);
        }

        while (!stack.isEmpty()) {
            output.add(stack.pop());
        }

        return output;
    }
}
