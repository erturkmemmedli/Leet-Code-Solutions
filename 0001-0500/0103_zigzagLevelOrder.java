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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> bfsZigzag = new ArrayList<>();
        if (root == null) return bfsZigzag;

        Queue<TreeNode> queue = new LinkedList<>() {{add(root);}};
        boolean isReversed = false;

        while (!queue.isEmpty()) {
            int length = queue.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < length; i++) {
                TreeNode node = queue.remove();
                level.add(node.val);
                
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }

            if (isReversed) Collections.reverse(level);

            isReversed ^= true;
            bfsZigzag.add(level);
        }

        return bfsZigzag;
    }
}
