class TreeNode {
    int val;
    TreeNode parent;
    TreeNode left;
    TreeNode right;
    int leftSize;
    int rightSize;
    int aboveSize;

    public TreeNode(int val) {
        this.val = val;
        this.parent = null;
        this.left = null;
        this.right = null;
        this.leftSize = 0;
        this.rightSize = 0;
        this.aboveSize = 0;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }

        TreeNode other = (TreeNode) obj;

        if (this.val != other.val) {
            return false;
        }

        boolean leftEquals = (this.left == null && other.left == null) || 
                             (this.left != null && this.left.equals(other.left));
        boolean rightEquals = (this.right == null && other.right == null) || 
                              (this.right != null && this.right.equals(other.right));
        boolean sizeEquals = (this.leftSize == other.leftSize) && 
                             (this.rightSize == other.rightSize) && 
                             (this.aboveSize == other.aboveSize);

        return leftEquals && rightEquals && sizeEquals;
    }

    @Override
    public int hashCode() {
        return Objects.hash(val, left, right, leftSize, rightSize, aboveSize);
    }

    @Override
    public String toString() {
        String leftStr = (left != null) ? "Left: " + left.val : "Left: null";
        String rightStr = (right != null) ? "Right: " + right.val : "Right: null";
        return "TreeNode{val=" + val + ", " + leftStr + ", " + rightStr + 
               ", leftSize=" + leftSize + ", rightSize=" + rightSize + ", aboveSize=" + aboveSize + "}";
    }
}

class Solution {
    public static long maxScore = 0;
    public static HashMap<Long, Integer> counter = new HashMap<>();

    public int countHighestScoreNodes(int[] parents) {
        int n = parents.length;
        TreeNode[] parentNodes = new TreeNode[n];

        for (int i = 0; i < n; i++) {
            parentNodes[i] = new TreeNode(i);
        }

        for (int i = 1; i < n; i++) {
            if (parentNodes[parents[i]].left == null) {
                parentNodes[parents[i]].left = parentNodes[i];
            } else {
                parentNodes[parents[i]].right = parentNodes[i];
            }

            parentNodes[i].parent = parentNodes[parents[i]];
            TreeNode temp = parentNodes[i];

            while (temp.parent != null) {
                if (temp == temp.parent.left) {
                    temp.parent.leftSize = temp.leftSize + temp.rightSize + 1;
                } else {
                    temp.parent.rightSize = temp.leftSize + temp.rightSize + 1;
                }

                temp = temp.parent;
            }
        }

        traverseTree(parentNodes[0]);

        int result = counter.get(maxScore);
        maxScore = 0;
        counter = new HashMap<>();
        
        return result;
    }

    public void traverseTree(TreeNode root) {
        if (root == null) {
            return;
        }

        if (root.left != null) {
            root.left.aboveSize = root.aboveSize + root.rightSize + 1;
        }

        if (root.right != null) {
            root.right.aboveSize = root.aboveSize + root.leftSize + 1;
        }

        int l = root.leftSize;
        int r = root.rightSize;
        int k = root.aboveSize;

        long score = (long)Math.max(l, 1) * (long)Math.max(r, 1) * (long)Math.max(k, 1);
        maxScore = Math.max(maxScore, score);
        counter.put(score, counter.getOrDefault(score, 0) + 1);

        traverseTree(root.left);
        traverseTree(root.right);
    }
}
