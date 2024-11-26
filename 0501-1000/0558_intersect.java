/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node() {}

    public Node(boolean _val,boolean _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
    public Node intersect(Node quadTree1, Node quadTree2) {
        if (quadTree1.isLeaf) {
            return quadTree1.val ? quadTree1 : quadTree2;
        } else if (quadTree2.isLeaf) {
            return quadTree2.val ? quadTree2 : quadTree1;
        } else {
            Node tLeft = intersect(quadTree1.topLeft, quadTree2.topLeft);
            Node tRight = intersect(quadTree1.topRight, quadTree2.topRight);
            Node bLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
            Node bRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight);

            boolean isLeaf = tLeft.isLeaf && tRight.isLeaf && bLeft.isLeaf && bRight.isLeaf;
            boolean equalVal = tLeft.val == tRight.val && tRight.val == bLeft.val && bLeft.val == bRight.val;
            
            if (isLeaf && equalVal) {
                return new Node(tLeft.val, true, null, null, null, null);
            } else {
                return new Node(false, false, tLeft, tRight, bLeft, bRight);
            }
        }
    }
}
