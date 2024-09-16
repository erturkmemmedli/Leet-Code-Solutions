/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> output = new ArrayList<>();

        if (root == null) return output;

        Queue<Node> queue = new LinkedList<>() {{add(root);}};

        while (!queue.isEmpty()) {
            int length = queue.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < length; i++) {
                Node node = queue.remove();
                level.add(node.val);

                for (Node child: node.children) {
                    queue.add(child);
                }
            }
            output.add(level);
        }

        return output;
    }
}
