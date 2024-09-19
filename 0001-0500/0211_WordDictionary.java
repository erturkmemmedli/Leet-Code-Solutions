class Node {
    HashMap<Character, Node> children;
    boolean isEnd;

    public Node() {
        this.children = new HashMap<>();
        this.isEnd = false;
    }
}

class WordDictionary {
    Node root;

    public WordDictionary() {
        this.root = new Node();
    }
    
    public void addWord(String word) {
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
    
    public boolean search(String word) {
        return dfs(this.root, word, 0);
    }

    public boolean dfs(Node node, String word, int index) {
        if (node.isEnd && index == word.length()) {
            return true;
        }
        if (!node.isEnd && index == word.length()) {
            return false;
        } 
        
        char c = word.charAt(index);
        
        if (c != '.' && !node.children.containsKey(c)) {
            return false;
        } else if (node.children.containsKey(c)) {
            return dfs(node.children.get(c), word, index + 1);
        } else {
            boolean[] result = {false};
            node.children.forEach((key, val) -> {
                result[0] = result[0] || dfs(node.children.get(key), word, index + 1);
            });
            return result[0];
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
