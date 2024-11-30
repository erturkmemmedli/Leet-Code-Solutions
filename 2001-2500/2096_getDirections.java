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
    public static String srcTarget = "";
    public static String dstTarget = "";
    public static boolean found = false;

    public String getDirections(TreeNode root, int startValue, int destValue) {
        dfs(root, startValue, destValue, startValue, new StringBuilder());
        found = false;
        dfs(root, startValue, destValue, destValue, new StringBuilder());
        found = false;

        int i = 0;
        StringBuilder result = new StringBuilder();

        while (i < Math.min(srcTarget.length(), dstTarget.length())) {
            if (srcTarget.charAt(i) != dstTarget.charAt(i)) {
                break;
            } 
            i++;
        }

        for (int j = i; j < srcTarget.length(); j++) {
            result.append("U");
        }

        for (int j = i; j < dstTarget.length(); j++) {
            result.append(dstTarget.charAt(j));
        }

        srcTarget = "";
        dstTarget = "";

        return result.toString();
    }

    public void dfs(TreeNode root, int startValue, int destValue, int target, StringBuilder path) {
        if (root == null || found) {
            return;
        }

        if (root.val == target) {
            if (target == startValue){
                srcTarget = path.toString();
            } else {
                dstTarget = path.toString();
            }
            found = true;
            return;
        }
        
        path.append("L");
        dfs(root.left, startValue, destValue, target, path);
        path.deleteCharAt(path.length() - 1); 
        path.append("R");
        dfs(root.right, startValue, destValue, target, path);
        path.deleteCharAt(path.length() - 1); 
    }
}
