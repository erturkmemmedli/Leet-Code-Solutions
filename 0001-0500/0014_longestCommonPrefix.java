class Node {
    HashMap<Character, Node> children;
    boolean isEnd;

    public Node() {
        this.children = new HashMap<>();
        this.isEnd = false;
    }
}

class Trie {
    Node root;

    public Trie() {
        this.root = new Node();
    }

    public void insert(String word) {
        Node node = this.root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (!node.children.containsKey(c)) {
                node.children.put(c, new Node());
            }

            node = node.children.get(c);
        }

        node.isEnd = true;
    }
}

class Solution {
    public String longestCommonPrefix(String[] strs) {
        Trie trie = new Trie();

        for(String str: strs) {
            if (str.isEmpty()) return "";
            trie.insert(str);
        }

        Node node = trie.root;
        StringBuilder result = new StringBuilder();

        while (true) {
            if (node.children.size() == 1) {
                char key = '*';
                for (char c: node.children.keySet()) {
                    key = c;
                    result.append(key);
                }
                node = node.children.get(key);
                if (node.isEnd) {
                    return result.toString();
                }
            } else {
                break; 
            }
        }
        return result.toString();
    }
}
