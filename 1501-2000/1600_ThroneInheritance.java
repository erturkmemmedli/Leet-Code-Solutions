/***
Successor(x, curOrder):
    if x has no children or all of x's children are in curOrder:
        if x is the king return null
        else return Successor(x's parent, curOrder)
    else return x's oldest child who's not in curOrder
***/

class Node {
    String name;
    String parent;
    Queue<Node> children;
    boolean isAlive;

    public Node(String name) {
        this.name = name;
        this.parent = null;
        this.children = new LinkedList<>();
        this.isAlive = true;
    }

    public Node(String name, String parentName) {
        this.name = name;
        this.parent = parentName;
        this.children = new LinkedList<>();
        this.isAlive = true;
    }
}

class ThroneInheritance {
    HashMap<String, Node> throneMap;
    Node king;

    public ThroneInheritance(String kingName) {
        this.throneMap = new HashMap<>();
        this.king = new Node(kingName);
        this.throneMap.put(kingName, king);
    }
    
    public void birth(String parentName, String childName) {
        Node node = new Node(childName, parentName);
        Node parent = throneMap.get(parentName);
        parent.children.add(node);
        throneMap.put(childName, node);
    }
    
    public void death(String name) {
        Node node = throneMap.get(name);
        node.isAlive = false;
    }
    
    public List<String> getInheritanceOrder() {
        List<String> result = new ArrayList<>();
        Node root = king;
        inorderDFS(root, result);
        return result;
    }

    public void inorderDFS(Node root, List<String> result) {
        if (root.isAlive) {
            result.add(root.name);
        }

        for (Node child: root.children) {
            inorderDFS(child, result);
        }
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = new ThroneInheritance(kingName);
 * obj.birth(parentName,childName);
 * obj.death(name);
 * List<String> param_3 = obj.getInheritanceOrder();
 */
