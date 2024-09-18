class TrieNode {
    HashMap<Character, TrieNode> children;
    boolean isEnd;

    public TrieNode() {
        this.children = new HashMap<>();
        this.isEnd = false;
    }
}


class Trie {
    TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = this.root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!node.children.containsKey(c)) {
                node.children.put(c, new TrieNode());
            }

            node = node.children.get(c);
        }

        node.isEnd = true;
    }
    
    public boolean search(String word) {
        TrieNode node = this.root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!node.children.containsKey(c)) {
                return false;
            }

            node = node.children.get(c);
        }

        return node.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = this.root;

        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (!node.children.containsKey(c)) {
                return false;
            }

            node = node.children.get(c);
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
