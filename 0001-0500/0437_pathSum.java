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
    public int count = 0;

    public int pathSum(TreeNode root, int targetSum) {
        dfs(root, (long)targetSum);
        return count;
    }

    public HashMap<Long, Integer> dfs(TreeNode root, long targetSum) {
        if (root == null) return new HashMap<>();

        HashMap<Long, Integer> left = dfs(root.left, targetSum);
        HashMap<Long, Integer> right = dfs(root.right, targetSum);
        HashMap<Long, Integer> total = new HashMap<>();

        total.put((long)root.val, total.getOrDefault((long)root.val, 0) + 1);
        count += total.getOrDefault(targetSum, 0);

        left.forEach((key, val) -> {
            long newVal = key + root.val;
            if (newVal == targetSum) count += val;
            total.put(newVal, total.getOrDefault(newVal, 0) + val);         
        });

        right.forEach((key, val) -> {
            long newVal = key + root.val;
            if (newVal == targetSum) count += val;
            total.put(newVal, total.getOrDefault(newVal, 0) + val);
        });

        return total;
    }
}

// Alternative solution

class Solution {
    public int count = 0;

    public int pathSum(TreeNode root, int targetSum) {
        HashMap<Long, Integer> memo = new HashMap<>(){{put(0L, 1);}};
        dfs(root, targetSum, memo, 0L);
        return count;
    }

    public void dfs(TreeNode root, int targetSum, HashMap<Long, Integer> memo, long currentSum) {
        if (root == null) {
            return;
        }

        currentSum += (long) root.val;
        count += memo.getOrDefault(currentSum - targetSum, 0);
        memo.put(currentSum, memo.getOrDefault(currentSum, 0) + 1);
        dfs(root.left, targetSum, memo, currentSum);
        dfs(root.right, targetSum, memo, currentSum);
        memo.put(currentSum, memo.getOrDefault(currentSum, 0) - 1);
    }
}
