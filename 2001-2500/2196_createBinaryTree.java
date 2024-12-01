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
    public TreeNode createBinaryTree(int[][] descriptions) {
        HashSet<Integer> rootNode = new HashSet<>();
        HashSet<Integer> unrootNodes = new HashSet<>();
        HashMap<Integer, TreeNode> treeNodes = new HashMap<>();

        for (int[] description: descriptions) {
            int parent = description[0], child = description[1], isLeft = description[2];

            if (!treeNodes.containsKey(parent)) {
                treeNodes.put(parent, new TreeNode(parent));
            }
            if (!treeNodes.containsKey(child)) {
                treeNodes.put(child, new TreeNode(child));
            }

            if (isLeft == 1) {
                treeNodes.get(parent).left = treeNodes.get(child);
            } else {
                treeNodes.get(parent).right = treeNodes.get(child);
            }

            unrootNodes.add(child);
            rootNode.remove(child);
            if (!unrootNodes.contains(parent)) {
                rootNode.add(parent);
            }
        }

        return treeNodes.get(rootNode.iterator().next());
    }
}
